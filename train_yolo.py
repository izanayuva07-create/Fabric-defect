# type: ignore
# pyright: reportMissingImports=false
"""
Train YOLOv8 to detect the 11 localized fabric defects:
Hole, Slub, Broken End, Broken Pick, Missing End, Float, Reed Mark,
Stain, Crease Mark, Pilling, Snag.

"Stain" is detected here as one class; src/inference_pipeline.py then crops
each Stain box and runs it through the TensorFlow stain sub-classifier to
resolve it into Oil Stain / Water Stain / Other Stain.

Start from a COCO-pretrained checkpoint (yolov8s.pt) and fine-tune on your
own labeled fabric images -- see the README for dataset options.
"""
from ultralytics import YOLO


def train(
    data_yaml: str = "../data/data.yaml",
    weights: str = "yolov8s.pt",
    epochs: int = 150,
    imgsz: int = 960,
    batch: int = 16,
):
    model = YOLO(weights)
    results = model.train(
        data=data_yaml,
        epochs=epochs,
        imgsz=imgsz,
        batch=batch,
        patience=25,
        project="runs/selvedge",
        name="yolov8_fabric_defects",
        # Color/brightness augmentation is toned down from YOLO's defaults
        # because shade and hue ARE defect signals in this domain -- we
        # don't want the model to learn to ignore them.
        hsv_h=0.010, hsv_s=0.4, hsv_v=0.25,
        degrees=5, shear=2, perspective=0.0002,
        mosaic=1.0, mixup=0.1,
        cos_lr=True,
        pretrained=True,
    )
    model.export(format="onnx")  # optional: portable format for serving
    return results


if __name__ == "__main__":
    train()
