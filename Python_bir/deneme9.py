from skimage import io, exposure
import matplotlib.pyplot as plt


img = io.imread('deneme.png')
#yeğinlik ölçekleme

# Define the minimum and maximum values
min_value = 0
max_value = 50

# Clamp the pixel values using the exposure.rescale_intensity function
img_clamped = exposure.rescale_intensity(img, in_range=(min_value/255, max_value/255), out_range=(0, 1))

# Display the original and clamped images side by side
fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(10, 5))
ax0.imshow(img, cmap='gray')
ax0.set_title('Original')
ax0.axis('off')
ax1.imshow(img_clamped, cmap='gray')
ax1.set_title('Clamped')
ax1.axis('off')

plt.show()