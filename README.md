# image-contours-detection

### Object Size Estimator with OpenCV

This Python project demonstrates **object size measurement** using OpenCV by analyzing contours in an image and calculating their dimensions based on a reference object. It can estimate the size of any detected object relative to the known dimensions of a reference object, like a coin or ruler.

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

5. **Bounding Rectangles**:
   - Calculates bounding rectangles or minimum enclosing shapes (like rotated rectangles) for the contours to determine their dimensions.

6. **Reference Object**:
   - Uses a reference object of a known size (like a coin) to calculate the **Pixel Per Metric (PPM)** ratio:
     \[
     \text{PPM} = \frac{\text{Pixels (measured width of reference object)}}{\text{Real-world width (inches or cm)}}
     \]

7. **Measure Other Objects**:
   - Uses the PPM ratio to estimate the size of all other objects in the image by scaling their pixel dimensions to real-world units.

---

## **Assumptions**
1. **Reference Object**:
   - The image contains a **reference object** whose dimensions (width or height) are known.
   - This object is easily distinguishable based on placement, color, or shape.
   
2. **Camera and Perspective**:
   - The image is a near **top-down view**, minimizing perspective distortions for accurate size calculations.

---

## **How It Works**
### Code Workflow:
1. **Input Parameters**:
   - Image path (e.g., `images/example_01.png`)
   - Known width of the reference object (e.g., `--width 0.955` for a U.S. quarter in inches).

2. **Detect Contours**:
   - Threshold the image and extract contours using:
     ```python
     contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
     ```
     
3. **Identify Reference Object**:
   - Locate the reference object in the contours (e.g., the quarter) and calculate the PPM ratio.

4. **Calculate Dimensions**:
   - Use the PPM ratio to estimate the real-world dimensions of the bounding boxes for all other contours.

5. **Display Results**:
   - Overlay dimensions and bounding boxes on the original image.

---

## **Required Libraries**
1. **Python**: 3.7+
2. **OpenCV**: Image processing and computer vision.
3. **NumPy**: Array manipulations for calculations.
4. **Imutils**: Utilities for contour sorting and bounding box manipulations.

---

## **Usage**
To measure object sizes using a reference object:
```bash
python object_size.py --image images/example_01.png --width 0.955
```

### Input:
- **`--image`**: Path to the input image containing the objects.
- **`--width`**: Real-world width of the reference object (e.g., 0.955 inches for a U.S. quarter).

---

## **Results**
The script outputs an annotated image showing:
1. **Bounding Boxes**:
   - Rectangles drawn around detected objects.
   
2. **Measured Dimensions**:
   - Width and height of each object displayed in real-world units.

---

## **Example Results**
1. **Input Image**:
   - Image containing multiple objects alongside the reference object.

2. **Output**:
   - Annotated image with each object’s dimensions.

---

## **Limitations**
1. **Top-Down Perspective**:
   - The input image must be a near **perfect top-down view** to minimize perspective distortion.

2. **Lens Distortion**:
   - Camera lens distortion can affect accuracy. Pre-calibration may improve results.

3. **Reference Object Accuracy**:
   - The accuracy of the measurements heavily depends on correctly identifying and using the reference object.

4. **Object Overlap**:
   - Overlapping objects may result in inaccurate contour detection.

---

This technique is a practical way to estimate object dimensions in controlled environments. It’s especially useful in scenarios where a known reference object can be included in the image for calibration.
