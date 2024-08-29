import cv2
import numpy as np

img = cv2.imread('assets/soccer_practice.jpg')
template = cv2.imread('assets/ball.png', 0)
)
h, w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img = img2.copy()
