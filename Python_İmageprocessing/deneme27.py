import numpy as np
import cv2

# Load the image
img = cv2.imread("huso2.jpg",cv2.IMREAD_GRAYSCALE)

# Define the mean and standard deviation for the Gaussian filter
mean = 0
std_dev = 0.9
#gaussian noisy  mean o stdv 40
gaussian_noise = np.zeros(img.shape, np.uint8)
cv2.randn(gaussian_noise, 0, 6)
noisy_img = cv2.add(img, gaussian_noise)


# Create the Gaussian filter
kernel_size = 5
kernel = cv2.getGaussianKernel(kernel_size, std_dev)
gaussian_filter = np.outer(kernel, kernel.transpose())

# Apply the Gaussian filter to the image
filtered_img = cv2.filter2D(noisy_img, -1, gaussian_filter)

# Display the original and filtered images side-by-side
cv2.imshow("Original Image", img)
cv2.imshow("Noisy Image", noisy_img)
cv2.imshow("Filtered Image", filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()