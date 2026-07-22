# Selvedge — Fabric Defect Detection Backend

A hybrid detection pipeline for 16 fabric defect types.

## Why hybrid, not YOLOv8 alone

11 of the 16 defects are localized to a specific spot on the fabric (a hole
is *at* some x/y). Those go through **YOLOv8**. The other 4 — Shade
Variation, Bow and Skew, Barré Effect, Shrinkage — are properties of the
whole swatch, not a bounding box, so they go through a **TensorFlow
multi-label classifier** run on the full frame instead. Stain is detected
as one YOLO class, then a small **TensorFlow sub-classifier** crops it and
decides Oil / Water / Other.

| Layer | Model | Detects |
|---|---|---|
| Spatial detector | YOLOv8s | Hole, Slub, Broken End, Broken Pick, Missing End, Float, Reed Mark, Stain, Crease Mark, Pilling, Snag |
| Stain sub-classifier | TensorFlow (MobileNetV3Small) | Oil Stain / Water Stain / Other Stain |
| Global classifier | TensorFlow (EfficientNetB0, multi-label) | Shade Variation, Bow and Skew, Barré Effect, Shrinkage |

## Important: there is no pretrained model for these exact classes

Nobody has published open weights trained on this specific 16-class
taxonomy — it's mill-specific vocabulary. `yolov8s.pt` and the
ImageNet-pretrained backbones give you a strong starting point (edges,
textures, shapes), but you need to **fine-tune on your own labeled fabric
images** before this detects anything real. Budget for that before the
judging deadline.

Fastest path to a working demo model:
1. Start with a public fabric-defect dataset to bootstrap training —
   **AITEX Fabric Defect Dataset** (fabric patches, several defect types),
   **TILDA-400** (textile texture/defect classes), or search Kaggle for
   "fabric defect detection dataset" — none map 1:1 onto your 16 classes,
   so you'll relabel/remap a subset.
2. Label with [Roboflow](https://roboflow.com) or LabelImg — export in
   YOLO format directly into `data/images/` + `data/labels/`.
3. For the stain sub-classifier, crop ~30-50 examples each of oil-stained
   and water-stained fabric (phone photos are fine) into
   `data/stain_crops/{train,val}/{oil,water,other}/`.
4. For the global classifier, put swatch photos in `data/global_labels/`
   with a CSV of 0/1 labels per class (a swatch can have more than one).
5. If you have almost no time left, train YOLO alone on 2-3 of the
   most visually distinct classes (Hole, Stain, Slub) for a live demo, and
   present the rest as "trained pipeline, awaiting labeled data" — that's
   an honest and still-impressive story for judges.

## Setup

```bash
pip install -r requirements.txt --break-system-packages   # if using system Python
```

## Train

```bash
cd src
python train_yolo.py                 # localized defects
python train_stain_classifier.py     # oil vs water vs other
python train_global_classifier.py    # whole-swatch defects
```

Trained weights land in `models/yolov8_fabric_defects.pt`,
`models/stain_classifier.keras`, `models/global_defect_classifier.keras`.

## Serve

```bash
python app.py
```

`POST /predict` with a multipart image under field `image` returns:

```json
{
  "image": "uploads/...",
  "defect_count": 2,
  "defects": [
    {"type": "Oil Stain", "bbox": [120, 80, 210, 160], "confidence": 0.91,
     "action": "Reject segment -- trace source to roller/lubrication point."},
    {"type": "Shade Variation", "bbox": null, "confidence": 0.73,
     "action": "Segregate roll -- dye lot mismatch, route to color-matching review."}
  ]
}
```

## Wire it to the frontend

In `frontend/selvedge.html`, replace the mock `finishScan()` logic with a
real `fetch('/predict', { method: 'POST', body: formData })` call and map
the returned `defects` array onto the results table and bounding-box
overlay — the JSON shape above already matches what the table expects
(`type`, `confidence`, `action`; use `bbox` to position overlay boxes,
`bbox: null` means it's a whole-swatch defect with no single location).
