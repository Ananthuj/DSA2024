import os
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator


# Function to load and preprocess the data
def load_data(data_dir, target_size=(150, 150), batch_size=32, validation_split=0.03):
    """Load and preprocess the data for training and validation."""
    datagen = ImageDataGenerator(rescale=1.0 / 255, validation_split=validation_split)

    train_generator = datagen.flow_from_directory(
        data_dir,
        target_size=target_size,
        batch_size=batch_size,
        class_mode="categorical",
        subset="training",
    )

    validation_generator = datagen.flow_from_directory(
        data_dir,
        target_size=target_size,
        batch_size=batch_size,
        class_mode="categorical",
        subset="validation",
    )

    return train_generator, validation_generator


# Function to create an enhanced CNN model with more layers
def create_model(input_shape=(150, 150, 3), num_classes=7):
    """Create a Sequential CNN model with extra layers."""
    model = Sequential(
        [
            Conv2D(32, (3, 3), activation="relu", input_shape=input_shape),
            MaxPooling2D(pool_size=(2, 2)),
            Conv2D(64, (3, 3), activation="relu"),
            MaxPooling2D(pool_size=(2, 2)),
            Conv2D(128, (3, 3), activation="relu"),
            MaxPooling2D(pool_size=(2, 2)),
            # Additional convolutional layers
            Conv2D(256, (3, 3), activation="relu"),
            MaxPooling2D(pool_size=(2, 2)),
            Conv2D(512, (3, 3), activation="relu"),
            MaxPooling2D(pool_size=(2, 2)),
            Flatten(),
            Dense(512, activation="relu"),
            Dropout(0.5),
            # Output layer for classification
            Dense(num_classes, activation="softmax"),
        ]
    )

    model.compile(
        loss="categorical_crossentropy",
        optimizer="adam",
        metrics=["accuracy"],
    )

    return model


# Function to train the model
def train_model(model, train_generator, validation_generator, epochs=30):
    """Train the model and return the training history."""
    history = model.fit(
        train_generator,
        validation_data=validation_generator,
        epochs=epochs,
        verbose=1,
    )
    return history


# Function to evaluate the model
def evaluate_model(model, validation_generator):
    """Evaluate the model on the validation set."""
    val_loss, val_acc = model.evaluate(validation_generator)
    print(f"Validation Loss: {val_loss}, Validation Accuracy: {val_acc}")
    return val_loss, val_acc


# Function to plot the training history
def plot_history(history):
    """Plot the training and validation accuracy and loss."""
    plt.figure(figsize=(10, 5))
    plt.plot(history.history["accuracy"], label="Train Accuracy")
    plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
    plt.title("Model Accuracy")
    plt.ylabel("Accuracy")
    plt.xlabel("Epoch")
    plt.legend(loc="upper left")
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.plot(history.history["loss"], label="Train Loss")
    plt.plot(history.history["val_loss"], label="Validation Loss")
    plt.title("Model Loss")
    plt.ylabel("Loss")
    plt.xlabel("Epoch")
    plt.legend(loc="upper left")
    plt.show()


# Function to save the model
def save_model(model, save_dir=".model", model_name="model.keras"):
    """Save the trained model."""
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    model_path = os.path.join(save_dir, model_name)
    model.save(model_path)
    print(f"Model saved at {model_path}")


# Main function to bring it all together
def main():
    data_dir = os.path.join(".data")

    # Load the data
    train_generator, validation_generator = load_data(data_dir)

    # Get the number of classes dynamically
    num_classes = train_generator.num_classes

    # Create the model with extra layers
    model = create_model(num_classes=num_classes)

    # Train the model
    history = train_model(model, train_generator, validation_generator)

    # Evaluate the model
    evaluate_model(model, validation_generator)

    # Plot the training history
    plot_history(history)

    # Save the model
    save_model(model)


# Run the main function
if __name__ == "__main__":
    main()
