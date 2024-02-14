import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('huso2.jpg',0) 
gray_range = [10, 200] # Set the range of gray levels to brighten

# Apply gray level slicing to the image
img_sliced = np.copy(img)
img_sliced[(img >= gray_range[0]) & (img <= gray_range[1])] += 50

# Display the original and the sliced image
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8,4))
axes[0].imshow(img, cmap='gray')
axes[0].set_title('Original Image')
axes[1].imshow(img_sliced, cmap='gray')
axes[1].set_title('Gray Level Sliced Image')
plt.show()