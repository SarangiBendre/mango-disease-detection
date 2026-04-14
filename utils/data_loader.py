from torchvision import datasets, transforms
from torch.utils.data import DataLoader

def load_data(data_dir):
    train_transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.RandomHorizontalFlip(),
        transforms.RandomVerticalFlip(),
        transforms.RandomRotation(30),
        transforms.ColorJitter(brightness=0.3, contrast=0.3),
        transforms.ToTensor(),
    ])

    test_transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])

    train_data = datasets.ImageFolder(root=data_dir + "/train", transform=train_transform)
    test_data = datasets.ImageFolder(root=data_dir + "/test", transform=test_transform)

    print("Class Mapping:", train_data.class_to_idx)

    train_loader = DataLoader(train_data, batch_size=16, shuffle=True)
    test_loader = DataLoader(test_data, batch_size=16, shuffle=False)

    return train_loader, test_loader, train_data.classes