import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import gdown
import zipfile

# Google Drive file ID and download using gdown
file_id = "1z1nFcsu_fcq44_qMOkK58qF2U5mPSC7H"
dataset_path = "dataset.zip"

# Download the dataset only if it doesn't exist
if not os.path.exists(dataset_path):
    try:
        gdown.download(
            f"https://drive.google.com/uc?id={file_id}", dataset_path, quiet=False
        )
    except Exception as e:
        print("Error downloading the dataset:", e)

# Unzip the dataset if not already extracted
data_dir = "data"
if not os.path.exists(data_dir):
    try:
        with zipfile.ZipFile(dataset_path, "r") as zip_ref:
            zip_ref.extractall(data_dir)
    except Exception as e:
        print("Error unzipping the dataset:", e)

# Directory where the dataset is located
current_dir = os.getcwd()
data_dir = os.path.join(current_dir, "data", "data")
# Create an ImageDataGenerator instance with rescaling
datagen = ImageDataGenerator(
    rescale=1.0 / 255, validation_split=0.2
)  # 20% for validation

# Load training data (80%)
train_generator = datagen.flow_from_directory(
    data_dir,
    target_size=(150, 150),  # Resize images to 150x150
    batch_size=32,  # Load 32 images per batch
    class_mode="categorical",  # Multi-class classification
    subset="training",  # Specify training subset
)

# Load validation data (20%)
validation_generator = datagen.flow_from_directory(
    data_dir,
    target_size=(150, 150),
    batch_size=32,
    class_mode="categorical",
    subset="validation",  # Specify validation subset
)

# Define the CNN model
model = Sequential(
    [
        Conv2D(
            32, (3, 3), activation="relu", input_shape=(150, 150, 3)
        ),  # First Conv Layer
        MaxPooling2D(pool_size=(2, 2)),  # Pooling Layer
        Conv2D(64, (3, 3), activation="relu"),  # Second Conv Layer
        MaxPooling2D(pool_size=(2, 2)),
        Conv2D(128, (3, 3), activation="relu"),  # Third Conv Layer
        MaxPooling2D(pool_size=(2, 2)),
        Flatten(),  # Flatten layer to convert 3D to 1D
        Dense(128, activation="relu"),  # Fully connected layer
        Dropout(0.5),  # Dropout to avoid overfitting
        Dense(5, activation="softmax"),  # Output layer (5 classes)
    ]
)

model.compile(
    loss="categorical_crossentropy",  # Suitable for multi-class classification
    optimizer="adam",  # Adam optimizer
    metrics=["accuracy"],  # Evaluate using accuracy
)

# Train the model
history = model.fit(
    train_generator,
    validation_data=validation_generator,  # Pass validation data directly
    epochs=10,  # Number of epochs (can adjust as needed)
    verbose=1,
)

# Evaluate the model
val_loss, val_acc = model.evaluate(validation_generator)
print(f"Validation Loss: {val_loss}, Validation Accuracy: {val_acc}")

# Plot training & validation accuracy and loss
plt.plot(history.history["accuracy"], label="Train Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.title("Model Accuracy")
plt.ylabel("Accuracy")
plt.xlabel("Epoch")
plt.legend(loc="upper left")
plt.show()

plt.plot(history.history["loss"], label="Train Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.title("Model Loss")
plt.ylabel("Loss")
plt.xlabel("Epoch")
plt.legend(loc="upper left")
plt.show()

# Save the model
tf.keras.models.save_model(model, "model.keras")
