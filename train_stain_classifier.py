# type: ignore
# pyright: reportMissingImports=false
"""
Stain sub-type classifier (TensorFlow / Keras 3 Engine).
Takes a cropped patch around each "Stain" box and classifies it as
Oil Stain, Water Stain, or Other Stain.
"""
import os
import sys
import numpy as np

# Set Keras backend to PyTorch for 100% native Python 3.14 execution
os.environ["KERAS_BACKEND"] = "torch"

try:
    import keras
    from keras import layers, models
except ImportError:
    print("[ERROR] 'keras' package is missing. Run: pip install keras")
    sys.exit(1)

IMG_SIZE = (128, 128)
CLASS_NAMES = ["Oil Stain", "Water Stain", "Other Stain"]


def build_model() -> keras.Model:
    inputs = layers.Input(shape=(*IMG_SIZE, 3))
    x = layers.Rescaling(1.0 / 255.0)(inputs)
    x = layers.Conv2D(32, (3, 3), activation="relu")(x)
    x = layers.MaxPooling2D((2, 2))(x)
    x = layers.Conv2D(64, (3, 3), activation="relu")(x)
    x = layers.MaxPooling2D((2, 2))(x)
    x = layers.Conv2D(128, (3, 3), activation="relu")(x)
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dropout(0.3)(x)
    outputs = layers.Dense(len(CLASS_NAMES), activation="softmax")(x)
    return models.Model(inputs, outputs)


def train(
    train_dir: str = "../data/stain_crops/train",
    val_dir: str = "../data/stain_crops/val",
    epochs: int = 15,
):
    print("[INFO] Building Keras Stain Classifier model...")
    model = build_model()
    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"],
    )

    models_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")
    os.makedirs(models_dir, exist_ok=True)
    os.makedirs("../models", exist_ok=True)

    save_path = os.path.join(models_dir, "stain_classifier.keras")
    model.save(save_path)
    print(f"[SUCCESS] Keras Stain Classifier compiled & saved to: '{save_path}'")
    return model


if __name__ == "__main__":
    train()
