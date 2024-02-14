import numpy as np
import cv2

# Load the image
img = cv2.imread('huso2.jpg', 0)

# Define noise probability
noise_prob = 0.05
#salt and pepper noisy 

# Generate random matrix with uniform distribution
noise_matrix = np.random.rand(*img.shape)

# Apply noise to the image
img_with_noise = img.copy()
img_with_noise[noise_matrix < noise_prob/2] = 0
img_with_noise[noise_matrix > 1 - noise_prob/2] = 255

# Display the images
cv2.imshow('Original', img)
cv2.imshow('Noisy', img_with_noise)
cv2.waitKey(0)
cv2.destroyAllWindows()