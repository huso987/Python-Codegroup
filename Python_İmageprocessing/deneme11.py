import cv2
import numpy as np

# Load the image in grayscale
img = cv2.imread('deneme.png')

# Define the gamma value
gamma = 1.3

# Perform gamma transformation
img_gamma = np.power(img, gamma)

# Normalize the image to 0-255 range
img_gamma = cv2.normalize(img_gamma, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)

# Display the original and gamma transformed images
cv2.imshow('Original', img)
cv2.imshow('Gamma Transformed', img_gamma)
cv2.waitKey(0)
cv2.destroyAllWindows()