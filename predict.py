import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# Load model
model = tf.keras.models.load_model("mango_model.h5")

# Class labels (IMPORTANT)
classes = ['anthracnose', 'healthy']

# Load test image
img_path = "test.jpg"   # change this to your image
img = image.load_img(img_path, target_size=(224, 224))

# Convert to array
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array / 255.0

# Predict
prediction = model.predict(img_array)
predicted_class = classes[np.argmax(prediction)]
confidence = np.max(prediction) * 100

# Output
print(f"Prediction: {predicted_class}")
print(f"Confidence: {confidence:.2f}%")