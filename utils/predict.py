import torch
from PIL import Image
import torchvision.transforms as transforms

device = torch.device("cpu")

def predict_image(img_path, model, class_names):
    transform = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor()
    ])

    image = Image.open(img_path).convert("RGB")
    image = transform(image).unsqueeze(0).to(device)

    model.eval()

    with torch.no_grad():
        output = model(image)
        probabilities = torch.softmax(output, dim=1)
        confidence, pred = torch.max(probabilities, 1)

    label = class_names[pred.item()]
    confidence = confidence.item() * 100

    # 🔥 Avoid wrong predictions
    if confidence < 60:
        return "uncertain", confidence

    return label, confidence