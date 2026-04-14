from flask import Flask, render_template, request, jsonify
import torch
import json
import os
from models.model import get_model
from utils.predict import predict_image

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load model
model = get_model()
model.load_state_dict(torch.load("models/mango_model.pth", map_location=torch.device('cpu')))
model.eval()

# Load class names
with open("models/classes.json", "r") as f:
    class_names = json.load(f)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']

    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        label, confidence = predict_image(filepath, model, class_names)

        return jsonify({
            "label": label,
            "confidence": round(confidence, 2),
            "image_path": filepath
        })

    return jsonify({"error": "No file uploaded"})

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)