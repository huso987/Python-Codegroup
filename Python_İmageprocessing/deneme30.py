import cv2
import numpy as np

# Using Median Filter on salt and pepper noise with image
I = cv2.imread('images.jpeg', cv2.IMREAD_GRAYSCALE)
noise_prob = 0.01
noise_matrix = np.random.rand(*I.shape)

# Apply noise to the image
img_with_noise = I.copy()
img_with_noise[noise_matrix < noise_prob/2] = 0
img_with_noise[noise_matrix > 1 - noise_prob/2] = 255
# Apply a 3x3 median filter to the image
J = cv2.medianBlur(img_with_noise, 3)

# Display the original and filtered images side-by-side
cv2.imshow('Original Image', I)
cv2.imshow('noise ',img_with_noise)
cv2.imshow('Filtered Image', J)
cv2.waitKey(0)
cv2.destroyAllWindows()
