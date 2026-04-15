# 🌿 Mango Leaf Anthracnose Disease Detection

This project detects **anthracnose disease in mango leaves** using **Deep Learning and Computer Vision**.
It provides accurate predictions along with confidence scores and preventive solutions for better crop management.

---

## 🚀 Live Demo

🌐 https://mango-disease-detection.onrender.com

> ⚠️ **Note:**
> The live demo is hosted on Render (free tier), so it may take a few seconds to respond during the first request or prediction due to limited resources.

---

## 🎥 Demo Video

▶️ https://youtu.be/f4g_xYH7dqY

---

## 📌 Features

* 📷 Upload mango leaf image
* 🔍 Detect disease (Healthy / Anthracnose)
* 📊 Confidence score display
* 🌿 Solution & prevention suggestions
* 📱 Mobile-friendly and responsive UI

---

## 🧠 Tech Stack

* **Backend:** Python (PyTorch, Flask)
* **Frontend:** HTML, CSS, JavaScript
* **Libraries:** OpenCV, Torchvision

---

## ⚙️ How It Works

1. User uploads a mango leaf image
2. Image is preprocessed (resizing and normalization)
3. Deep learning model analyzes the image
4. Prediction is generated with confidence score
5. If disease is detected → solution is displayed

---

## 📂 Project Structure

```
MangoLeafDiseaseDetection/
│
├── models/
│   ├── mango_model.pth
│   ├── classes.json
│   └── model.py
│
├── utils/
│   └── predict.py
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── uploads/
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
└── Procfile
```

---

## 🧪 Model Details

* Model: CNN (MobileNetV2-based)
* Framework: PyTorch
* Classes: Healthy, Anthracnose
* Accuracy: ~90%

---

## ⚠️ Limitations

* Limited dataset (150 images)
* May misclassify similar patterns
* Performance depends on image quality

---

## 🔮 Future Scope

* Add detection for more plant diseases
* Increase dataset size for better accuracy
* Develop mobile application
* Enable real-time detection using camera

---

## 🌱 Real-World Impact

This system helps farmers to:

* Detect diseases at an early stage
* Take preventive actions quickly
* Improve crop yield and quality

---

## 👨‍💻 Author

**Sarangi Bendre**

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
