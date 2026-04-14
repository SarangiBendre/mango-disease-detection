import torch.nn as nn
from torchvision import models
from torchvision.models import MobileNet_V2_Weights

def get_model():
    weights = MobileNet_V2_Weights.DEFAULT
    model = models.mobilenet_v2(weights=weights)

    # Freeze all layers
    for param in model.features.parameters():
        param.requires_grad = False

    # 🔥 Unfreeze last 3 layers for better learning
    for param in model.features[-3:].parameters():
        param.requires_grad = True

    # Replace classifier
    model.classifier[1] = nn.Linear(model.last_channel, 2)

    return model