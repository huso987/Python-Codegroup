import matplotlib.pyplot as plt
from skimage import io, exposure

# Load the input image
img = io.imread('huso2.jpg')

# Plot the input image and its histogram
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10,5))
ax1.imshow(img, cmap='gray')
ax1.set_title('Input Image')
ax2.hist(img.ravel(), bins=256, range=(0, 255), alpha=0.5, color='b')
ax2.set_title('Input Image Histogram')
ax2.set_xlim([0, 255])
ax2.set_ylim([0, 10000])
#isttogram eşitleme
# Apply histogram equalization to the input image
img_eq = exposure.equalize_hist(img)

# Plot the equalized image and its histogram
fig, (ax3, ax4) = plt.subplots(nrows=1, ncols=2, figsize=(10,5))
ax3.imshow(img_eq, cmap='gray')
ax3.set_title('Equalized Image')
ax4.hist(img_eq.ravel(), bins=256, range=(0, 1), alpha=0.5, color='b')
ax4.set_title('Equalized Image Histogram')
ax4.set_xlim([0, 1])
ax4.set_ylim([0, 10000])

plt.show()