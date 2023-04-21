import cv2

# Load the image
img = cv2.imread('huso2.jpg')

# Set window center and width values
window_center = 128
window_width = 64

# Apply intensity windowing using cv2.normalize function
min_value = window_center - window_width/2
max_value = window_center + window_width/2
img_windowed = cv2.normalize(img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# Display the original and windowed images
cv2.imshow('Original Image', img)
cv2.imshow('Windowed Image', img_windowed)
cv2.waitKey(0)
cv2.destroyAllWindows()
