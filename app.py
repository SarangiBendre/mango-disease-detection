from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import os

app = Flask(__name__)

# Load model
model = tf.keras.models.load_model("mango_model.h5")

classes = ['anthracnose', 'healthy']


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']

    if file.filename == '':
        return "No file selected"

    filepath = os.path.join("static", file.filename)
    file.save(filepath)

    img = image.load_img(filepath, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    prediction = model.predict(img_array)
    predicted_class = classes[np.argmax(prediction)]
    confidence = np.max(prediction) * 100

    return render_template(
        'index.html',
        prediction=predicted_class,
        confidence=round(confidence, 2),
        img_path=filepath
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)