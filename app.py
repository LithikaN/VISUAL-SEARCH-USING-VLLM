import sys
sys.path.append(r"C:\Users\lithi\food_tracker\food_tracker")  # Ensure the correct path

from detect_food import detect_food

print(detect_food())  # Test the function

import sys
sys.path.append(r"C:\Users\lithi\food_tracker\food_tracker")  # Ensure the correct path

from diet_plan import diet_plan

print(diet_plan())  # Test the function

#######################################


from flask import Flask, render_template, request, jsonify
import os
from detect_food import detect_food
from diet_plan import diet_plan

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"

# Ensure upload folder exists
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400

    file = request.files["image"]
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)

    # Detect food
    detected_food = detect_food(file_path)
    diet_plan = diet_plan(detected_food, "weight_loss")

    return render_template("index.html", image=file.filename, food=detected_food, diet=diet_plan)

if __name__ == "__main__":
    app.run(debug=True)

______________________________________________

import os
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Define the folder where uploaded images will be saved
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Route to handle image upload
@app.route("/upload", methods=["POST"])
def upload_file():
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400

    file = request.files["image"]
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)  
    file.save(file_path)

    return jsonify({"message": "File uploaded successfully", "file_path": file_path})

if __name__ == "__main__":
    app.run(debug=True)


#####################################

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask is running successfully!"

if __name__ == "__main__":
    print("Starting Flask App...")  # Debug print
    app.run()
