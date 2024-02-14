
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
img = cv2.imread('images.jpeg', 0)

# Define the Laplacian filter
laplacian_filter = np.array([[0, -1, 0],
                             [-1, 4, -1],
                             [0, -1, 0]])

# Apply the filter using the cv2.filter2D() function
filtered_img = cv2.filter2D(img, -1, laplacian_filter)

# Display the original and filtered images side-by-side
plt.subplot(1,2,1), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2), plt.imshow(filtered_img, cmap='gray')
plt.title('Filtered Image'), plt.xticks([]), plt.yticks([])
plt.show()