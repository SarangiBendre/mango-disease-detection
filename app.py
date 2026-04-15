from flask import Flask, render_template, request, jsonify
import torch
import json
import os
from PIL import Image
from models.model import get_model
from utils.predict import predict_image

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 🔥 Load model ONLY ONCE
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
    try:
        file = request.files['file']

        if not file:
            return jsonify({"error": "No file uploaded"})

        # Save file
        filepath = os.path.join(UPLOAD_FOLDER, "temp.jpg")
        file.save(filepath)

        # 🔥 Resize image (IMPORTANT for speed)
        img = Image.open(filepath).convert("RGB")
        img = img.resize((256, 256))
        img.save(filepath)

        print("Prediction started...")

        label, confidence = predict_image(filepath, model, class_names)

        print("Prediction done:", label)

        return jsonify({
            "label": label,
            "confidence": round(confidence, 2)
        })

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)})