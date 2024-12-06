import matplotlib.pyplot as plt
import cv2
import numpy as np

# Read image
image = cv2.imread("./images/newyork.jpg")

# Convert image to gray image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Binarization process
_, thresh = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)

# Draw contours on the original image
contour_image = image.copy()
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 3)

# Out contour image
plt.imshow(cv2.cvtColor(contour_image, cv2.COLOR_BGR2RGB))
plt.title("Contours Detected")
plt.axis("off")
plt.show()

