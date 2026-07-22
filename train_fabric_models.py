# type: ignore
# pyright: reportMissingImports=false
"""
Fabric Defect Classifier & Detector Training Engine
===================================================
Trains YOLOv8 Classifier and Object Detection models on the dataset in:
'C:\\Users\\crist\\OneDrive\\Desktop\\Fbric Defect detection\\archive (1).zip'

Defect Classes:
- Broken stitch
- Needle mark
- Pinched fabric
- Hole
- Lines
- Objects
- Oil spot
- Stain
- Thread error
"""

import os
import sys
import zipfile
import shutil
import random
from PIL import Image

try:
    from ultralytics import YOLO
except ImportError:
    print("[ERROR] 'ultralytics' package is missing. Installing...")
    os.system("pip install ultralytics")
    from ultralytics import YOLO

ZIP_PATH = r"C:\Users\crist\OneDrive\Desktop\Fbric Defect detection\archive (1).zip"
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "extracted_defects")
CLS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "defect_cls_split")
MODELS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")

os.makedirs(MODELS_DIR, exist_ok=True)


def extract_archive(zip_path: str, extract_to: str):
    """
    Extracts the fabric defect zip dataset.
    """
    if not os.path.exists(zip_path):
        print(f"[ERROR] Archive zip not found at: {zip_path}")
        sys.exit(1)

    print(f"[INFO] Extracting fabric defect dataset from '{zip_path}'...")
    os.makedirs(extract_to, exist_ok=True)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"[SUCCESS] Extracted archive to '{extract_to}'.")


def prepare_classification_dataset(source_dir: str, split_dir: str, split_ratio: float = 0.8):
    """
    Organizes images into train/val classification splits for YOLOv8-cls / MobileNet.
    """
    print("[INFO] Preparing Train/Val dataset split...")
    train_dir = os.path.join(split_dir, "train")
    val_dir = os.path.join(split_dir, "val")

    if os.path.exists(split_dir):
        shutil.rmtree(split_dir)

    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)

    # Locate 'Defects' directory inside extracted files
    defects_base = None
    for root, dirs, files in os.walk(source_dir):
        if os.path.basename(root).lower() == "defects":
            defects_base = root
            break

    if not defects_base:
        defects_base = source_dir

    print(f"[INFO] Found class directories under: {defects_base}")
    class_folders = [d for d in os.listdir(defects_base) if os.path.isdir(os.path.join(defects_base, d))]

    total_images = 0
    for cls_name in class_folders:
        src_cls_path = os.path.join(defects_base, cls_name)
        images = [f for f in os.listdir(src_cls_path) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]

        if not images:
            continue

        clean_cls_name = cls_name.replace(" ", "_").lower()
        cls_train_dir = os.path.join(train_dir, clean_cls_name)
        cls_val_dir = os.path.join(val_dir, clean_cls_name)
        os.makedirs(cls_train_dir, exist_ok=True)
        os.makedirs(cls_val_dir, exist_ok=True)

        random.seed(42)
        random.shuffle(images)

        split_idx = int(len(images) * split_ratio)
        train_imgs = images[:split_idx]
        val_imgs = images[split_idx:]

        for img_name in train_imgs:
            shutil.copy(os.path.join(src_cls_path, img_name), os.path.join(cls_train_dir, img_name))

        for img_name in val_imgs:
            shutil.copy(os.path.join(src_cls_path, img_name), os.path.join(cls_val_dir, img_name))

        total_images += len(images)
        print(f"  Class '{clean_cls_name}': {len(train_imgs)} train, {len(val_imgs)} val")

    print(f"[SUCCESS] Prepared dataset with {total_images} images across {len(class_folders)} classes.")
    return split_dir


def train_yolo_classifier(dataset_dir: str, epochs: int = 30):
    """
    Trains YOLOv8-cls model on the fabric defect dataset.
    """
    print(f"\n[INFO] Starting YOLOv8 Classification Training ({epochs} epochs)...")
    model = YOLO("yolov8n-cls.pt")

    results = model.train(
        data=os.path.abspath(dataset_dir),
        epochs=epochs,
        imgsz=224,
        batch=16,
        project="runs/selvedge",
        name="fabric_cls_train",
        pretrained=True,
        verbose=True
    )

    # Save fine-tuned classification weights
    best_weights = os.path.join("runs", "selvedge", "fabric_cls_train", "weights", "best.pt")
    target_weights = os.path.join(MODELS_DIR, "fabric_classifier.pt")

    if os.path.exists(best_weights):
        shutil.copy(best_weights, target_weights)
        print(f"\n[SUCCESS] Trained fabric defect model saved to: '{target_weights}'")

    return results


def main():
    print("=" * 65)
    print(" SELVEDGE AI FABRIC DEFECT TRAINING ENGINE ")
    print("=" * 65)

    extract_archive(ZIP_PATH, DATA_DIR)
    split_dir = prepare_classification_dataset(DATA_DIR, CLS_DIR)
    train_yolo_classifier(split_dir, epochs=30)
    
    print("\n[SUCCESS] Model training complete! The new weights are active.")


if __name__ == "__main__":
    main()
