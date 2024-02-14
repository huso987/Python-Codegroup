
import numpy as np
import matplotlib.pyplot as plt
import cv2
# Load the "pout.tif" image
img = cv2.imread('huso2.jpg',0)

# Set the threshold range for gray level slicing
threshold_low = 80
threshold_high = 200

# Create a binary mask based on the threshold range
mask = np.logical_and(img >= threshold_low, img <= threshold_high)

# Apply gray level slicing to the image
img_sliced = img.copy()
img_sliced[mask] = 255

# Display the original and gray level sliced images
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(img, cmap='gray')
ax1.set_title('Original Image')
ax2.imshow(img_sliced, cmap='gray')
ax2.set_title('Gray Level Sliced Image')
plt.show()