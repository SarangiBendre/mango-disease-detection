# 🌿 Mango Leaf Disease Detection using AI

## 📌 Overview

This project is a Computer Vision-based web application that detects diseases in mango leaves using a trained Deep Learning model. It helps identify plant health status from images, making it useful for agriculture and students.

---

## 🎯 Objective

To develop an intelligent system that:

* Detects mango leaf diseases from images
* Classifies leaves as Healthy or Anthracnose
* Displays prediction with confidence score
* Provides an easy-to-use web interface

---

## 🧠 Technologies Used

* Python
* TensorFlow (Deep Learning)
* OpenCV (Image Processing)
* Flask (Web Framework)
* HTML, CSS (Frontend)

---

## ⚙️ Features

* Upload mango leaf image
* Automatic image preprocessing
* Disease prediction using trained CNN model
* Confidence score display
* Clean and interactive UI
* Loading animation for better UX

---

## 📂 Project Structure

```
MangoLeafDiseaseDetection/
│
├── app.py
├── mango_model.h5
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
```

---

## 🚀 How to Run

### 1️⃣ Install dependencies

```
pip install tensorflow==2.10.0 flask numpy pillow opencv-python
```

### 2️⃣ Run the application

```
python app.py
```

### 3️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

## 📊 Output

* Predicted Disease (Healthy / Anthracnose)
* Confidence Percentage
* Uploaded Image Preview

---

## 🧪 Dataset

* Custom dataset (self-collected images)
* 16 images for Healthy
* 16 images for Anthracnose
* Used for training CNN model

---

## ⚠️ Limitations

* Small dataset size
* Limited to two classes
* Works best on clear leaf images

---

## 🔮 Future Enhancements

* Add more diseases
* Increase dataset size
* Deploy optimized model online
* Mobile application integration

---

## 🏆 Conclusion

This project demonstrates how AI and Computer Vision can be applied to plant disease detection. It provides a simple and effective solution for identifying mango leaf diseases.

---

## 👩‍💻 Author

Sarangi Bendre

---

## 📌 Note

This project is implemented locally due to compatibility constraints of TensorFlow on cloud platforms.
