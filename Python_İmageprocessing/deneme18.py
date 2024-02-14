import cv2

# Load the image in grayscale
img = cv2.imread('huso2.jpg', 0)

# Set the threshold range for gray level slicing
threshold_low = -60
threshold_high = 200

# Create a binary mask based on the threshold range
mask = cv2.inRange(img, threshold_low, threshold_high)

# Apply gray level slicing to the image
img_sliced = img.copy()
img_sliced[mask != 255] = 1

# Display the original image and the sliced image
cv2.imshow('Original', img)
cv2.imshow('Sliced', img_sliced)
cv2.waitKey(0)
cv2.destroyAllWindows()