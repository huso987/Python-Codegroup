import cv2
import numpy as np

# resmi oku ve diziye dönüştür
img = cv2.imread('deneme.png')
img = np.array(img)

# Gaussian gürültüsü ekle
mean = 0
var = 25
sigma = var ** 0.5
gaussian = np.random.normal(mean, sigma, (img.shape[0], img.shape[1], img.shape[2]))
gaussian = gaussian.reshape(img.shape[0], img.shape[1], img.shape[2]).astype('uint8')
noisy_image = cv2.addWeighted(img, 0.5, gaussian, 0.5, 0)

# gürültülü resmi göster
cv2.imshow('Noisy Image', noisy_image)
cv2.waitKey(0)
cv2.destroyAllWindows()