import torch
from torchvision import models, transforms
from PIL import Image
import requests

# 1. Tayyor modelni yuklaymiz
model = models.resnet18(pretrained=True)
model.eval()  # test (inference) rejim

# 2. Rasmni tayyorlash (transform)
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225]),
])

# 3. Rasmni yuklash va transform qilish
img_path = "Dog_1.jpg"
image = Image.open(img_path).convert("RGB")
img_tensor = transform(image).unsqueeze(0)  # (1, 3, 224, 224)

# 4. Modeldan bashorat olish
with torch.no_grad():
    output = model(img_tensor)
    predicted_class_id = output.argmax().item()

# 5. Class nomini olish
# ImageNet label fayl (0–999)
LABELS_URL = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
labels = requests.get(LABELS_URL).text.strip().split("\n")
predicted_label = labels[predicted_class_id]

print(f"Rasm: {img_path}")
print(f"Topilgan klass: {predicted_label} ({predicted_class_id})")
