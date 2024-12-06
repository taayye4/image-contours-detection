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
