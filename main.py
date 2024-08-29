import cv2
import numpy as np

img = cv2.imread('assets/soccer_practice.jpg')
template = cv2.imread('assets/ball.png', 0)
img2 = img.copy()
h, w = template.shape
(height, width)
