import cv2
import numpy as np

# Load the image
img = cv2.imread('huso2.jpg', cv2.IMREAD_GRAYSCALE)

# Add Gaussian noise
mean = 0
var = 0.01
sigma = var**0.5
gauss = np.random.normal(mean, sigma, (img.shape))
noisy_img = np.clip(img + gauss*255, 0, 255).astype(np.uint8)

# Apply 5x5 averaging filter
kernel_size = 5
kernel = np.ones((kernel_size,kernel_size),np.float32)/kernel_size**2
filtered_img = cv2.filter2D(noisy_img,-1,kernel)

# Display the results
cv2.imshow('Original Image', img)
cv2.imshow('Noisy Image', noisy_img)
cv2.imshow('Filtered Image', filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()