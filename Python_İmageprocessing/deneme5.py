import cv2
import numpy as np

# İki resmi yükleme
img1 = cv2.imread('deneme.png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('denme.png', cv2.IMREAD_GRAYSCALE)

# İki resmi binary formata dönüştürme
_, img1_binary = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)
_, img2_binary = cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY)

# İki resmi binary AND işlemiyle birleştirme
result = cv2.bitwise_and(img1_binary, img2_binary)
#result = cv2.bitwise_or(img1_binary, img2_binary)
# Sonucu gösterme
cv2.imshow('Binary AND', result)
cv2.waitKey(0)
cv2.destroyAllWindows()