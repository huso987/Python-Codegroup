import cv2
import numpy as np

# Load the image
img = cv2.imread('huso2.jpg',0)
noise_prob = 0.001
noise_matrix = np.random.rand(*img.shape)

# Apply noise to the image
img_with_noise = img.copy()
img_with_noise[noise_matrix < noise_prob/2] = 0
img_with_noise[noise_matrix > 1 - noise_prob/2] = 255

# Define the kernel for the weighted filter
kernel = np.array([[3, 5, 3],
                   [5, 8, 5],
                   [3, 5, 3]]) / 40.0

# Apply the filter to the image
filtered_img = cv2.filter2D(img_with_noise, -1, kernel)

# Display the original and filtered images
cv2.imshow('Original Image', img)
cv2.imshow('Noisy  Image', img_with_noise)
cv2.imshow('Filtered Image', filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()