# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 12:44:19 2025

@author: lithi
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/detect_food", methods=["POST"])
def detect_food_api():
    """API endpoint for detecting food and generating diet plans."""
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400

    file = request.files["image"]
    file_path = "input.jpg"
    file.save(file_path)

    detected_food = detect_food(file_path)
    diet_plan = generate_diet_plan(detected_food)
    
    

    return jsonify({"food": detected_food, "diet_plan": diet_plan})

if __name__ == "__main__":
    app.run()

def recognize_food(image_path):
    # Dummy function (Replace this with real ML model inference)
    return "Pizza"  # Example detected food
