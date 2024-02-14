import cv2
import numpy as np


#kontrast genişletme
img = cv2.imread('huso2.jpg', cv2.IMREAD_GRAYSCALE)

# Determine the intensity range for contrast stretching using np.percentile
low, high = np.percentile(img, (0,1))
img_stretched = cv2.normalize(img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# Perform contrast stretching
img_stretched = cv2.equalizeHist(img_stretched)

# Display the original image and the stretched image
cv2.imshow('Original Image', img)
cv2.imshow('Stretched Image', img_stretched)
cv2.waitKey(0)
cv2.destroyAllWindows()