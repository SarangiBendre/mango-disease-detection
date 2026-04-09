import gradio as gr
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# Load model
model = tf.keras.models.load_model("mango_model.h5")

classes = ['anthracnose', 'healthy']

def predict(img):
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    class_name = classes[np.argmax(prediction)]
    confidence = float(np.max(prediction)) * 100

    return f"{class_name} ({confidence:.2f}%)"

# Gradio UI
interface = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="🌿 Mango Disease Detection",
    description="Upload a mango leaf image to detect disease"
)

interface.launch()