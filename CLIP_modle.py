import matplotlib.pyplot as plt
import cv2
import numpy as np
from transformers import CLIPProcessor, CLIPModel

# CLIP 모델 및 프로세서 로드
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# 이미지 로드 및 OpenCV로 변환
image = cv2.imread("./images/newyork.jpg")
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
