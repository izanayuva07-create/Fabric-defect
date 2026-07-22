# type: ignore
# pyright: reportMissingImports=false
"""
YOLOv8 & TensorFlow-compatible Object Detection Inference Engine
================================================================
This script performs real-time object detection on Images, Video files, and live Webcam streams.

MODEL ARCHITECTURE & FRAMEWORK SELECTION:
- YOLOv8 (via Ultralytics) is chosen as the primary object detection engine.
- Rationale: Benchmark evaluations demonstrate YOLOv8 consistently outperforms legacy
  TensorFlow Object Detection API models (such as SSD MobileNet v2 or Faster R-CNN) in both
  Inference Latency (FPS) and Mean Average Precision (mAP50-95).
- Framework Integration: YOLOv8 uses PyTorch under the hood for model execution, but weights can
  also be exported to ONNX, TensorFlow SavedModel, TFLite, or TensorRT formats via `model.export(format='saved_model')`.

USAGE EXAMPLES:
1. Image Inference:
   python detect.py --image input.jpg --output output.jpg --conf 0.25

2. Video File Inference:
   python detect.py --video input.mp4 --output output.mp4 --conf 0.30

3. Live Webcam Stream Inference:
   python detect.py --webcam --cam-id 0 --conf 0.25
"""

import argparse
import os
import sys
import time
import cv2
import numpy as np

try:
    from ultralytics import YOLO
except ImportError:
    print("Error: 'ultralytics' package is not installed.")
    print("Please install required packages using: pip install ultralytics opencv-python pillow torch")
    sys.exit(1)


def load_detection_model(model_path: str = "yolov8n.pt"):
    """
    Loads a pre-trained YOLOv8 object detection model.
    Downloads official PyTorch weights automatically if local weights file is not found.
    """
    print(f"[INFO] Loading Object Detection Model from: '{model_path}'...")
    try:
        model = YOLO(model_path)
        print("[INFO] Model loaded successfully.")
        return model
    except Exception as e:
        print(f"[ERROR] Failed to load model from '{model_path}': {e}")
        sys.exit(1)


def draw_custom_bounding_boxes(frame: np.ndarray, results, conf_thresh: float = 0.25) -> np.ndarray:
    """
    Draws styled bounding boxes, class labels, and confidence scores on an image frame.
    """
    annotated_frame = frame.copy()
    
    for result in results:
        boxes = result.boxes
        if boxes is None or len(boxes) == 0:
            continue
            
        for box in boxes:
            confidence = float(box.conf[0])
            if confidence < conf_thresh:
                continue

            # Extract bounding box coordinates [x1, y1, x2, y2]
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls_id = int(box.cls[0])
            class_name = result.names.get(cls_id, f"Class {cls_id}")
            
            # Generate vibrant color based on class ID
            color = (
                int((cls_id * 50 + 40) % 256),
                int((cls_id * 80 + 100) % 256),
                int((cls_id * 120 + 160) % 256)
            )

            # Draw rectangle box
            cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), color, 2)

            # Prepare text label string
            label = f"{class_name}: {confidence * 100:.1f}%"
            (font_w, font_h), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)

            # Draw text background banner
            cv2.rectangle(
                annotated_frame,
                (x1, max(0, y1 - font_h - 6)),
                (x1 + font_w + 6, max(font_h + 6, y1)),
                color,
                -1
            )
            # Render white label text
            cv2.putText(
                annotated_frame,
                label,
                (x1 + 3, max(font_h + 2, y1 - 3)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (255, 255, 255),
                1,
                cv2.LINE_AA
            )

    return annotated_frame


def detect_on_image(model, image_path: str, output_path: str = None, conf_thresh: float = 0.25):
    """
    Performs object detection on a single input image.
    """
    if not os.path.exists(image_path):
        print(f"[ERROR] Input image file '{image_path}' does not exist.")
        return

    print(f"[INFO] Processing image: '{image_path}'...")
    image = cv2.imread(image_path)
    if image is None:
        print(f"[ERROR] Could not read image file: '{image_path}'")
        return

    # Run YOLOv8 inference
    results = model.predict(source=image, conf=conf_thresh, verbose=False)
    
    # Render bounding boxes
    output_image = draw_custom_bounding_boxes(image, results, conf_thresh)

    # Print detected objects count
    total_detections = sum(len(r.boxes) for r in results if r.boxes is not None)
    print(f"[SUCCESS] Found {total_detections} detected object(s).")

    # Save output if path is specified
    if output_path:
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        cv2.imwrite(output_path, output_image)
        print(f"[INFO] Annotated image saved to: '{output_path}'")
    else:
        try:
            cv2.imshow("Object Detection Result", output_image)
            print("[INFO] Press any key to close the window...")
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except Exception as err:
            fallback_out = "detected_output.jpg"
            cv2.imwrite(fallback_out, output_image)
            print(f"[INFO] GUI display unavailable ({err}). Saved result to '{fallback_out}'.")


def detect_on_video(model, video_path: str, output_path: str = None, conf_thresh: float = 0.25):
    """
    Performs object detection on a video file.
    """
    if not os.path.exists(video_path):
        print(f"[ERROR] Input video file '{video_path}' does not exist.")
        return

    print(f"[INFO] Opening video file: '{video_path}'...")
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"[ERROR] Failed to open video file: '{video_path}'")
        return

    # Extract video parameters
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0

    writer = None
    if output_path:
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
        print(f"[INFO] Saving processed video stream to: '{output_path}'")

    frame_count = 0
    print("[INFO] Starting video frame inference. Press 'q' to stop early...")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        # Perform detection frame by frame
        results = model.predict(source=frame, conf=conf_thresh, verbose=False)
        annotated_frame = draw_custom_bounding_boxes(frame, results, conf_thresh)

        if writer:
            writer.write(annotated_frame)

        try:
            cv2.imshow("Video Object Detection", annotated_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("[INFO] Stream interrupted by user.")
                break
        except Exception:
            pass

    cap.release()
    if writer:
        writer.release()
    try:
        cv2.destroyAllWindows()
    except Exception:
        pass
    print(f"[SUCCESS] Processed {frame_count} frames.")


def detect_on_webcam(model, cam_id: int = 0, output_path: str = None, conf_thresh: float = 0.25):
    """
    Performs real-time object detection from a live webcam feed.
    """
    print(f"[INFO] Initializing webcam camera device #{cam_id}...")
    cap = cv2.VideoCapture(cam_id)

    if not cap.isOpened():
        print(f"[ERROR] Cannot access camera device index {cam_id}.")
        print("[TIP] Ensure your camera is plugged in and allowed by OS security settings.")
        return

    # Try setting 1280x720 capture resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = 30.0

    writer = None
    if output_path:
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
        print(f"[INFO] Recording live webcam stream to: '{output_path}'")

    print("[INFO] Live Webcam Object Detection is active.")
    print("[INFO] Press 'q' or ESC in the preview window to exit.")

    prev_time = time.time()
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("[WARNING] Empty frame received from webcam stream.")
            continue

        # Inference
        results = model.predict(source=frame, conf=conf_thresh, verbose=False)
        annotated_frame = draw_custom_bounding_boxes(frame, results, conf_thresh)

        # Calculate FPS
        curr_time = time.time()
        fps_val = 1.0 / max(1e-5, curr_time - prev_time)
        prev_time = curr_time

        # Overlay FPS on stream
        cv2.putText(
            annotated_frame,
            f"FPS: {fps_val:.1f}",
            (15, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            2,
            cv2.LINE_AA
        )

        if writer:
            writer.write(annotated_frame)

        try:
            cv2.imshow("Live Webcam AI Inspection Feed", annotated_frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == 27:  # 'q' or ESC
                print("[INFO] Exiting webcam feed...")
                break
        except Exception:
            pass

    cap.release()
    if writer:
        writer.release()
    try:
        cv2.destroyAllWindows()
    except Exception:
        pass


def main():
    parser = argparse.ArgumentParser(
        description="YOLOv8 & TensorFlow Real-time Object Detection CLI (Image, Video & Webcam)"
    )
    
    parser.add_argument("--image", type=str, help="Path to input image file.")
    parser.add_argument("--video", type=str, help="Path to input video file.")
    parser.add_argument("--webcam", action="store_true", help="Use live webcam stream as input.")
    parser.add_argument("--cam-id", type=int, default=0, help="Camera device index (default: 0).")
    parser.add_argument("--output", type=str, help="Path to save output image or video.")
    parser.add_argument("--model", type=str, default="yolov8n.pt", help="Path to YOLOv8 model weights (.pt or .onnx).")
    parser.add_argument("--conf", type=float, default=0.25, help="Confidence threshold score (0.0 to 1.0).")

    args = parser.parse_args()

    # Load object detection model
    model = load_detection_model(args.model)

    # Route execution based on command line arguments
    if args.image:
        detect_on_image(model, args.image, args.output, args.conf)
    elif args.video:
        detect_on_video(model, args.video, args.output, args.conf)
    elif args.webcam:
        detect_on_webcam(model, args.cam_id, args.output, args.conf)
    else:
        print("[WARNING] No input source specified! Defaulting to live webcam mode...")
        detect_on_webcam(model, args.cam_id, args.output, args.conf)


if __name__ == "__main__":
    main()
