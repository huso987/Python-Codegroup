import cv2
import numpy as np
#intensity windowing
img = cv2.imread('huso2.jpg',0)
window_center = 128
window_width = 64
img_adjusted = cv2.normalize(img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
img_adjusted = cv2.convertScaleAbs(img_adjusted, alpha=window_width/255, beta=window_center-window_width/2)

cv2.imshow('Original Image', img)
cv2.imshow('Adjusted Image', img_adjusted)
cv2.waitKey(0)
cv2.destroyAllWindows()