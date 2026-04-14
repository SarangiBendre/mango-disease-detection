import torch
import torch.nn as nn
import torch.optim as optim
import json
from utils.data_loader import load_data
from models.model import get_model

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

train_loader, test_loader, class_names = load_data("dataset")

model = get_model().to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.0001)

epochs = 12

for epoch in range(epochs):
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0

    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

        # 🔥 Training accuracy
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

    train_acc = 100 * correct / total
    print(f"Epoch {epoch+1}/{epochs}, Loss: {running_loss:.4f}, Train Acc: {train_acc:.2f}%")

print("Training Complete!")

# ✅ Test Accuracy
model.eval()
correct = 0
total = 0

with torch.no_grad():
    for images, labels in test_loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)

        _, predicted = torch.max(outputs, 1)

        total += labels.size(0)
        correct += (predicted == labels).sum().item()

accuracy = 100 * correct / total
print(f"Test Accuracy: {accuracy:.2f}%")

# 💾 Save model
torch.save(model.state_dict(), "models/mango_model.pth")

# 💾 Save class names
with open("models/classes.json", "w") as f:
    json.dump(class_names, f)

print("Model + Classes saved!")