import os
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms, models

DATA_DIR = r"c:\Users\crist\OneDrive\Desktop\Fbric Defect detection\data\defect_cls_split"
MODEL_SAVE_PATH = r"c:\Users\crist\OneDrive\Desktop\Fbric Defect detection\models\fabric_classifier.pt"

os.makedirs(os.path.dirname(MODEL_SAVE_PATH), exist_ok=True)

transform_train = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

train_dataset = datasets.ImageFolder(os.path.join(DATA_DIR, "train"), transform=transform_train)
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True, num_workers=0)

class_names = train_dataset.classes
print(f"[INFO] Training fabric neural network on {len(class_names)} classes: {class_names}")

model = models.mobilenet_v2(pretrained=True)
model.classifier[1] = nn.Linear(model.last_channel, len(class_names))

device = torch.device("cpu")
model.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.002)

model.train()
for epoch in range(1):
    running_loss = 0.0
    correct = 0
    total = 0
    for imgs, labels in train_loader:
        imgs, labels = imgs.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(imgs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item() * imgs.size(0)
        _, preds = torch.max(outputs, 1)
        total += labels.size(0)
        correct += torch.sum(preds == labels.data)

    print(f"Completed Epoch 1/1 - Loss: {running_loss/total:.4f} | Accuracy: {correct.double()/total:.4f}")

torch.save({
    'model_state_dict': model.state_dict(),
    'class_names': class_names
}, MODEL_SAVE_PATH)

print(f"[SUCCESS] Fabric classifier weights saved to: {MODEL_SAVE_PATH}")
