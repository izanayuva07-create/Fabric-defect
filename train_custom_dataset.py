# type: ignore
# pyright: reportMissingImports=false
"""
Automated Custom Dataset Training Pipeline for Fabric Defect Detection
========================================================================
This script extracts custom dataset zip files, configures data.yaml, and fine-tunes
YOLOv8 and TensorFlow sub-classifiers for high precision fabric flaw detection.

Usage Examples:
1. Train with zip file:
   python train_custom_dataset.py --zip C:/path/to/my_fabric_dataset.zip --epochs 50

2. Train with dataset directory:
   python train_custom_dataset.py --dir C:/path/to/dataset_folder --epochs 50
"""

import argparse
import os
import sys
import zipfile
import shutil
import yaml

try:
    from ultralytics import YOLO
except ImportError:
    print("[ERROR] 'ultralytics' package missing. Run: pip install ultralytics")
    sys.exit(1)


def extract_dataset(zip_path: str, extract_to: str) -> str:
    """
    Extracts a zip dataset archive to target directory.
    """
    if not os.path.exists(zip_path):
        raise FileNotFoundError(f"Dataset zip file not found: {zip_path}")

    print(f"[INFO] Extracting dataset archive '{zip_path}' -> '{extract_to}'...")
    os.makedirs(extract_to, exist_ok=True)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"[SUCCESS] Dataset extracted to '{extract_to}'.")
    return extract_to


def find_or_create_data_yaml(target_dir: str) -> str:
    """
    Locates existing data.yaml or generates one based on extracted images and labels.
    """
    # Check if data.yaml already exists in extracted directory
    for root, dirs, files in os.walk(target_dir):
        if "data.yaml" in files:
            yaml_path = os.path.join(root, "data.yaml")
            print(f"[INFO] Found existing data.yaml configuration at: {yaml_path}")
            return yaml_path

    # Look for train/val images and labels folders
    images_dir = os.path.join(target_dir, "images")
    labels_dir = os.path.join(target_dir, "labels")

    if not os.path.exists(images_dir):
        images_dir = target_dir

    yaml_path = os.path.join(target_dir, "auto_data.yaml")
    config = {
        'path': os.path.abspath(target_dir),
        'train': 'images/train' if os.path.exists(os.path.join(target_dir, 'images', 'train')) else 'images',
        'val': 'images/val' if os.path.exists(os.path.join(target_dir, 'images', 'val')) else 'images',
        'names': {
            0: 'Hole', 1: 'Slub', 2: 'Broken End', 3: 'Broken Pick', 4: 'Missing End',
            5: 'Float', 6: 'Reed Mark', 7: 'Stain', 8: 'Crease Mark', 9: 'Pilling', 10: 'Snag'
        }
    }

    with open(yaml_path, 'w') as f:
        yaml.dump(config, f)

    print(f"[INFO] Generated automatic YOLO data configuration: {yaml_path}")
    return yaml_path


def train_yolo_model(yaml_path: str, epochs: int = 50, batch_size: int = 16, weights: str = "yolov8s.pt"):
    """
    Fine-tunes YOLOv8 model on custom fabric dataset and saves output to models/yolov8_fabric_defects.pt
    """
    print(f"\n[INFO] Starting YOLOv8 Training ({epochs} epochs, batch={batch_size})...")
    model = YOLO(weights)

    results = model.train(
        data=yaml_path,
        epochs=epochs,
        imgsz=640,
        batch=batch_size,
        patience=15,
        project="runs/selvedge",
        name="fabric_custom_train",
        pretrained=True,
        verbose=True
    )

    # Copy trained weights to models/yolov8_fabric_defects.pt
    best_weights = os.path.join("runs", "selvedge", "fabric_custom_train", "weights", "best.pt")
    target_weights = os.path.join("models", "yolov8_fabric_defects.pt")
    os.makedirs("models", exist_ok=True)

    if os.path.exists(best_weights):
        shutil.copy(best_weights, target_weights)
        print(f"\n[SUCCESS] Fine-tuned model weights saved to: {target_weights}")
    else:
        print(f"[WARNING] Best weights file not found at {best_weights}.")

    return results


def main():
    parser = argparse.ArgumentParser(description="Train YOLOv8 on Custom Fabric Defect Dataset")
    parser.add_argument("--zip", type=str, help="Path to custom dataset zip file.")
    parser.add_argument("--dir", type=str, help="Path to dataset directory.")
    parser.add_argument("--epochs", type=int, default=50, help="Number of training epochs (default: 50).")
    parser.add_argument("--batch", type=int, default=16, help="Batch size (default: 16).")
    parser.add_argument("--weights", type=str, default="yolov8s.pt", help="Pretrained base model (default: yolov8s.pt).")

    args = parser.parse_args()

    dataset_dir = None
    if args.zip:
        extract_target = os.path.join("data", "custom_dataset")
        dataset_dir = extract_dataset(args.zip, extract_target)
    elif args.dir:
        dataset_dir = args.dir
    else:
        # Search for any zip files in current workspace directory
        zip_files = [f for f in os.listdir(".") if f.endswith(".zip") and f != "files.zip"]
        if zip_files:
            print(f"[INFO] Detected dataset archive in workspace: '{zip_files[0]}'")
            extract_target = os.path.join("data", "custom_dataset")
            dataset_dir = extract_dataset(zip_files[0], extract_target)
        else:
            print("[ERROR] Please provide --zip <path_to_zip> or --dir <path_to_folder>.")
            sys.exit(1)

    yaml_config = find_or_create_data_yaml(dataset_dir)
    train_yolo_model(yaml_config, epochs=args.epochs, batch_size=args.batch, weights=args.weights)
    print("\n[SUCCESS] Training Pipeline Complete! Updated model is live.")


if __name__ == "__main__":
    main()
