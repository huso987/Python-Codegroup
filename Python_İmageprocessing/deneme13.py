import cv2

# Load the image in grayscale
img = cv2.imread('deneme.png',0)

# Apply adaptive thresholding with a block size of 11 and a constant value of 2
img_thresholded = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Display the original and thresholded images
cv2.imshow('Original', img)
cv2.imshow('Adaptive Thresholded', img_thresholded)
cv2.waitKey(0)
cv2.destroyAllWindows()