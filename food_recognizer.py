import os
import openvino.runtime as ov
import cv2
import numpy as np
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"

# Ensure the upload folder exists
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# Load OpenVINO model
ie = ov.Core()
model_path = "mobilenet-v2-pytorch.xml"
compiled_model = ie.compile_model(model_path, "CPU")

# Food class labels (Example)
class_labels = ["apple", "banana", "burger", "pizza", "sandwich", "pasta", "salad", "sushi"]

def preprocess_image(image_path):
    """Load and preprocess the image for the model."""
    image = cv2.imread(image_path)
    image = cv2.resize(image, (224, 224))  # Resize to model's input size
    image = image.astype(np.float32) / 255.0  # Normalize
    image = np.transpose(image, (2, 0, 1))  # Convert to NCHW format
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

def recognize_food(image_path):
    """Predict the food category."""
    input_tensor = preprocess_image(image_path)
    output = compiled_model(input_tensor)
    predictions = output[compiled_model.outputs[0]]  # Get output tensor
    predicted_label = np.argmax(predictions)  # Get highest probability class index
    return class_labels[predicted_label]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "image" not in request.files:
            return jsonify({"error": "No image uploaded"}), 400
        
        file = request.files["image"]
        if file.filename == "":
            return jsonify({"error": "No selected file"}), 400
        
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(file_path)

        # Detect food
        detected_food = recognize_food(file_path)

        return jsonify({"food": detected_food, "message": f"Detected food: {detected_food}"})
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
