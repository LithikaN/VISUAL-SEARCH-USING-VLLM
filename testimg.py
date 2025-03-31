# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 12:45:43 2025

@author: lithi
"""

import requests

url = "http://127.0.0.1:5000/detect_food"
image_path = "C:/Users/lithi/food_tracker/food_tracker/food 3.jpg"

with open(image_path, "rb") as img:
    files = {"image": img}
    response = requests.post(url, files=files)

print(response.json())
