# 🌿 Mango Leaf Anthracnose Disease Detection

This project detects **anthracnose disease in mango leaves** using **Deep Learning and Computer Vision**.
It provides accurate predictions along with confidence scores and preventive solutions.

---

## 🚀 Live Demo

🌐 https://mango-disease-detection.onrender.com

---

## 🎥 Demo Video

▶️ https://youtu.be/f4g_xYH7dqY

---

## 📌 Features

* 📷 Upload mango leaf image
* 🔍 Detect disease (Healthy / Anthracnose)
* 📊 Confidence score display
* 🌿 Solution & prevention suggestions
* 📱 Mobile-friendly UI

---

## 🧠 Tech Stack

* Python (PyTorch)
* Flask
* OpenCV
* HTML, CSS, JavaScript

---

## ⚙️ How It Works

1. User uploads a mango leaf image
2. Image is preprocessed (resized, normalized)
3. Deep learning model analyzes the image
4. Prediction is generated with confidence score
5. If disease detected → solution is displayed

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
* Accuracy: ~90%+

---

## ⚠️ Limitations

* Limited dataset (150 images)
* May misclassify similar patterns
* Works best with clear leaf images

---

## 🔮 Future Scope

* Add more diseases
* Improve dataset size
* Mobile app integration
* Real-time detection using camera

---

## 🌱 Real-World Impact

This system helps farmers:

* Detect disease early
* Take preventive actions
* Improve crop yield

---

## 👨‍💻 Author

**Sarangi Bendre**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
