import cv2
import numpy as np
# Görüntü yükleme
img = cv2.imread('huso2.jpg',0)
filter_sizes = [3, 5, 21]
noise_prob = 0.001
#salt and pepper noisy eklenmiş görüntüyü filtreleme yöntemi ile yumuşatma
# Generate random matrix with uniform distribution
noise_matrix = np.random.rand(*img.shape)

# Apply noise to the image
img_with_noise = img.copy()
img_with_noise[noise_matrix < noise_prob/2] = 0
img_with_noise[noise_matrix > 1 - noise_prob/2] = 255


cv2.imshow('Original', img)
cv2.imshow('Noisy', img_with_noise)
for size in filter_sizes:
    # Filtreyi tanımla
    kernel = np.ones((size, size), np.float32) / (size ** 2)
    # Filtreyi resme uygula
    filtered_img = cv2.filter2D(img_with_noise, -1, kernel)
    # Resimleri göster
    cv2.imshow(f'Filtered Image ({size}x{size})', filtered_img)

cv2.waitKey(0)
cv2.destroyAllWindows()