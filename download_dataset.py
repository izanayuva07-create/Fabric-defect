# type: ignore
# pyright: reportMissingImports=false
import os
import sys
import kagglehub

print("[INFO] Downloading dataset 'renukasiriwardhana/fabric-defect-dataset' via kagglehub...")
path = kagglehub.dataset_download("renukasiriwardhana/fabric-defect-dataset")
print(f"[SUCCESS] Dataset downloaded to: {path}")

# Print directory contents
print("\n[INFO] Dataset Contents:")
for root, dirs, files in os.walk(path):
    rel_root = os.path.relpath(root, path)
    print(f"\nDirectory: {rel_root}")
    if dirs:
        print(f"  Subdirectories: {dirs[:10]}")
    if files:
        print(f"  Sample Files ({len(files)} total): {files[:5]}")
