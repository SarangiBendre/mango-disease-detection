from flask import Flask, render_template, request, jsonify
import torch
import json
import os
from PIL import Image
from models.model import get_model
from utils.predict import predict_image

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 🔥 Load model ONLY ONCE (correct)
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

        # 🔥 Save file safely
        filepath = os.path.join(UPLOAD_FOLDER, "temp.jpg")
        file.save(filepath)

        # 🔥 Reduce image size BEFORE prediction (VERY IMPORTANT)
        img = Image.open(filepath).convert("RGB")
        img = img.resize((256, 256))  # reduce heavy image
        img.save(filepath)

        print("Prediction started...")  # debug

        # 🔥 Predict
        label, confidence = predict_image(filepath, model, class_names)

        print("Prediction done:", label)  # debug

        return jsonify({
            "label": label,
            "confidence": round(confidence, 2)
        })

    except Exception as e:
        print("Error:", str(e))  # logs in Render
        return jsonify({"error": str(e)})

# 🔥 Required for Render
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)