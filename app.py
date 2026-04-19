from flask import Flask, render_template, request, jsonify
import torch
import json
import os
from PIL import Image
from utils.predict import predict_image

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 🔥 Load OPTIMIZED model (TorchScript)
model = torch.jit.load("models/mango_model_scripted.pt")
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

        filepath = os.path.join(UPLOAD_FOLDER, "temp.jpg")
        file.save(filepath)

        # 🔥 Smaller image = faster
        img = Image.open(filepath).convert("RGB")
        img = img.resize((128, 128))
        img.save(filepath)

        print("⚡ Fast Prediction started...")

        label, confidence = predict_image(filepath, model, class_names)

        print("✅ Prediction done:", label)

        return jsonify({
            "label": label,
            "confidence": round(confidence, 2)
        })

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)})

# For local run
if __name__ == '__main__':
    app.run(debug=True)