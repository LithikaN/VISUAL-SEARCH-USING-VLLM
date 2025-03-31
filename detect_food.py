def detect_food():
    return "Food detection is working!"

import openvino.runtime as ov
import cv2
import numpy as np

# Load OpenVINO Model
ie = ov.Core()
model = ie.read_model("mobilenet-v2-pytorch.xml")
compiled_model = ie.compile_model(model, "CPU")

# Food Classes (Example)
FOOD_CLASSES = ["apple", "banana", "burger", "pizza", "salad"]

def detect_food(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (224, 224))
    image = np.expand_dims(image, axis=0)

    # Run inference
    result = compiled_model.infer_new_request({0: image})[0]

    # Get predicted class
    predicted_class = FOOD_CLASSES[np.argmax(result)]
    return predicted_class
