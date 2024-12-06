import matplotlib.pyplot as plt
import cv2
import numpy as np

# read image
image = cv2.imread("./images/newyork.jpg")

# convert image to gray image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# binarization process
_, thresh = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)
