import matplotlib.pyplot as plt
import cv2
import numpy as np
from transformers import CLIPProcessor, CLIPModel

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

image = cv2.imread("./images/newyork.jpg")
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

inputs = processor(
    text=["a photo of a horse", "a photo of a dog", "a photo of a bear", "a photo of a person", "a photo of a building"], 
    images=rgb_image,
    return_tensors="pt", 
    padding=True
)

outputs = model(**inputs)
logits_per_image = outputs.logits_per_image
probs = logits_per_image.softmax(dim=1)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contour_image = image.copy()
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 3)

fig, axs = plt.subplots(1, 2, figsize=(12, 6))

axs[0].imshow(rgb_image)
axs[0].set_title(
    f"Probabilities: horse: {probs[0, 0]:.2f}, dog: {probs[0, 1]:.2f}, "
    f"bear: {probs[0, 2]:.2f}, person: {probs[0, 3]:.2f}, building: {probs[0, 4]:.2f}"
)
axs[0].axis("off")

axs[1].imshow(cv2.cvtColor(contour_image, cv2.COLOR_BGR2RGB))
axs[1].set_title("Contours Detected")
axs[1].axis("off")

plt.tight_layout()
plt.show()
