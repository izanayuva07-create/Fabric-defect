# type: ignore
# pyright: reportMissingImports=false
"""
Whole-fabric global defect classifier (TensorFlow / Keras 3 Engine).
Multi-label classifier over the full frame for Shade Variation, Bow & Skew,
Barre Effect, and Shrinkage.
"""
import os
import sys

# Set Keras backend to PyTorch for native execution
os.environ["KERAS_BACKEND"] = "torch"

try:
    import keras
    from keras import layers, models
except ImportError:
    print("[ERROR] 'keras' package is missing. Run: pip install keras")
    sys.exit(1)

IMG_SIZE = (384, 384)
CLASS_NAMES = ["Shade Variation", "Bow and Skew", "Barre Effect", "Shrinkage"]


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
    outputs = layers.Dense(len(CLASS_NAMES), activation="sigmoid")(x)
    return models.Model(inputs, outputs)


def train(
    epochs: int = 15,
):
    print("[INFO] Building Keras Global Defect Classifier model...")
    model = build_model()
    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["binary_accuracy"],
    )

    models_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")
    os.makedirs(models_dir, exist_ok=True)
    os.makedirs("../models", exist_ok=True)

    save_path = os.path.join(models_dir, "global_defect_classifier.keras")
    model.save(save_path)
    print(f"[SUCCESS] Keras Global Defect Classifier compiled & saved to: '{save_path}'")
    return model


if __name__ == "__main__":
    train()
