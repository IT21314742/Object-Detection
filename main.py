import cv2
import numpy as np

# Load images
img = cv2.imread('assets/soccer_practice.jpg')
template = cv2.imread('assets/ball.png', 0)  # Grayscale template
h, w = template.shape  # Get dimensions of the template

# Convert main image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Define methods for template matching
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()  # Copy the original image for drawing rectangles

    # Perform template maching
    result = cv2.matchTemplate(img_gray, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    # Choose location based on the 
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:

        location = min_loc
    else:   
        location = max_loc

    # Define bottom-right corner of the rectangle
    bottom_right = (location[0] + w, location[1] + h)

    # Draw a rectangle around the detected region
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    
    # Display the result for each method
    cv2.imshow(f'Match - Method: {method}', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
