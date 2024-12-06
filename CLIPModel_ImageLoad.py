import matplotlib.pyplot as plt
import cv2
import numpy as np
from transformers import CLIPProcessor, CLIPModel

# CLIP Model and Processor Loads
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Load images and convert to OpenCV
image = cv2.imread("./images/newyork.jpg")
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Load the CLIP model and processor
inputs = processor(
    text=["a photo of a horse", "a photo of a dog", "a photo of a bear", "a photo of a person", "a photo of a building"], 
    images=rgb_image,
    return_tensors="pt", 
    padding=True
)

# Run CLIP model prediction
outputs = model(**inputs)
logits_per_image = outputs.logits_per_image
probs = logits_per_image.softmax(dim=1)

# Print the probabilities
print(f"Probabilities: horse: {probs[0, 0]:.2f}, dog: {probs[0, 1]:.2f}, "
      f"bear: {probs[0, 2]:.2f}, person: {probs[0, 3]:.2f}, building: {probs[0, 4]:.2f}")
