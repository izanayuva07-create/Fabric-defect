# type: ignore
# pyright: reportMissingImports=false
"""
Flask API wrapping the inference pipeline for the Selvedge frontend.
POST /predict with an image file under form field "image" or JSON base64 data -> JSON defect report.
"""
import os
import sys
import uuid
import base64

# Add local directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, jsonify, request, send_from_directory
from werkzeug.utils import secure_filename

try:
    from flask_cors import CORS
    has_cors = True
except ImportError:
    has_cors = False

try:
    from inference_pipeline import inspect, load_models
except ImportError:
    from src.inference_pipeline import inspect, load_models

app = Flask(__name__)
if has_cors:
    CORS(app)

UPLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Lazy loading or initial loading of models
yolo, stain_clf, global_clf = None, None, None

def get_models():
    global yolo, stain_clf, global_clf
    if yolo is None:
        try:
            yolo, stain_clf, global_clf = load_models()
        except Exception as e:
            print(f"Warning: Could not pre-load model weights: {e}")
    return yolo, stain_clf, global_clf


@app.route("/predict", methods=["POST"])
def predict():
    y_mod, s_mod, g_mod = get_models()
    
    # Read conf_thresh parameter (default sensitive threshold = 0.25)
    conf_thresh = 0.25
    if request.args.get("conf_thresh"):
        try:
            conf_thresh = float(request.args.get("conf_thresh"))
        except ValueError:
            pass
    elif request.form.get("conf_thresh"):
        try:
            conf_thresh = float(request.form.get("conf_thresh"))
        except ValueError:
            pass
    elif request.is_json and request.json and "conf_thresh" in request.json:
        try:
            conf_thresh = float(request.json["conf_thresh"])
        except (ValueError, TypeError):
            pass

    path = None
    if "image" in request.files:
        file = request.files["image"]
        sec_name = secure_filename(file.filename) if file.filename else "upload.jpg"
        filename = f"{uuid.uuid4().hex}_{sec_name}"
        path = os.path.join(UPLOAD_DIR, filename)
        file.save(path)
    elif request.is_json and request.json and "image_base64" in request.json:
        data = request.json["image_base64"]
        if "," in data:
            data = data.split(",", 1)[1]
        img_bytes = base64.b64decode(data)
        filename = f"{uuid.uuid4().hex}_webcam.jpg"
        path = os.path.join(UPLOAD_DIR, filename)
        with open(path, "wb") as f:
            f.write(img_bytes)
    else:
        return jsonify({"error": "No image file under form field 'image' or 'image_base64' JSON field."}), 400

    try:
        report = inspect(path, y_mod, s_mod, g_mod, conf_thresh=conf_thresh)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(report)


@app.route("/", methods=["GET"])
@app.route("/selvedge.html", methods=["GET"])
def serve_index():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), "selvedge.html")


@app.route("/<path:filename>", methods=["GET"])
def serve_static(filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    if os.path.exists(os.path.join(base_dir, filename)):
        return send_from_directory(base_dir, filename)
    elif os.path.exists(os.path.join(UPLOAD_DIR, filename)):
        return send_from_directory(UPLOAD_DIR, filename)
    return jsonify({"error": "File not found"}), 404


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "models_loaded": yolo is not None})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
