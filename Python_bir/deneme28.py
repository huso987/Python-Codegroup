import cv2
import numpy as np

# Load the image
img = cv2.imread('images.jpeg')

# Define the filter size and standard deviation
filter_size = 5
sigma = 6
gaussian_noise = np.zeros(img.shape, np.uint8)
cv2.randn(gaussian_noise, 0, 100)
noisy_img = cv2.add(img, gaussian_noise)

# Create the Gaussian filter
gaussian_filter = cv2.getGaussianKernel(filter_size, sigma)

# Apply the filter to each color channel separately
filtered_image = cv2.filter2D(noisy_img, -1, gaussian_filter)
filtered_image[:,:,0] = cv2.filter2D(noisy_img[:,:,0], -1, gaussian_filter)
filtered_image[:,:,1] = cv2.filter2D(noisy_img[:,:,1], -1, gaussian_filter)
filtered_image[:,:,2] = cv2.filter2D(noisy_img[:,:,2], -1, gaussian_filter)

# Display the original and filtered images side-by-side
cv2.imshow('Original Image', img)
cv2.imshow('Noisy image',noisy_img)
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()