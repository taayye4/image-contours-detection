# image-contours-detection

### Contour Detection with OpenCV

This Python project demonstrates **Contour Detection** using OpenCV in an image. 

---

## **Key Steps in the Process**
1. **Convert the Image to Grayscale**:
   - Converts the input image to grayscale to simplify further processing.
   
2. **Thresholding**:
   - Applies binary thresholding to separate the objects from the background.

3. **Contour Detection**:
   - Detects the edges or outlines of objects in the image using OpenCV’s `findContours()`.

4. **Draw Detected Contours**:
   - Draws the detected contours over the original image for visualization.

---


## **How It Works**
### Code Workflow:
1. **Input Parameters**:
   - Image path (e.g., `images/example_01.png`)

2. **Detect Contours**:
   - Threshold the image and extract contours using:
     ```python
     contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
     ```
     
5. **Display Results**:
   - Display image with highlighted contours.

---

## **Required Libraries**
1. **Python**: 3.7+
2. **OpenCV**: Image processing and computer vision.
3. **NumPy**: Array manipulations for calculations.
4. **Matplotlib**: Utilities for displaying.
5. **Transformers**: Image model CLIP and processing.

---

## **Results**
The script outputs an annotated image showing:
1. **Highlighted Contours**:
   - Contours drawn around objects in image.

---
