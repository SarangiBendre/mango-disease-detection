import torch
from models.model import get_model

model = get_model()
model.load_state_dict(torch.load("models/mango_model.pth", map_location="cpu"))
model.eval()

scripted_model = torch.jit.script(model)
scripted_model.save("models/mango_model_scripted.pt")

print("✅ Model optimized and saved!")