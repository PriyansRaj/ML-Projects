import torch
import cv2
from PIL import Image
import numpy as np
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import torch.nn as nn

class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.hidden = nn.Linear(784, 128)     
        self.output = nn.Linear(128, 10)      
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.hidden(x))
        x = self.output(x)
        return x
model= NeuralNetwork()
model.load_state_dict(torch.load('Mnist1.pth'))
model.eval()


img= Image.open("3.png")
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),
    transforms.Resize((28,28)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,),(0.5,))
])

img_tensor = transform(img)
img_tensor = img_tensor.view(-1, 28*28)



with torch.no_grad():
    output = model(img_tensor)
    _, predicted = torch.max(output, 1)
    print(f'Predicted digit: {predicted.item()}')

plt.imshow(np.array(img), cmap='gray')
plt.title(f"Predicted Number: {predicted.item()}")
plt.show()