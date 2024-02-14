import cv2
import numpy as np

# Resmi yükle
img = cv2.imread('deneme.png')

# Çarpanı tanımla
alpha = 0.5

# Çarpma işlemi
bright_img = np.clip(alpha * img, 0, 255).astype('uint8')

# Orijinal ve parlaklık arttırılmış resimleri göster
cv2.imshow('Orijinal Resim', img)
cv2.imshow('Parlaklık Arttırılmış Resim', bright_img)
cv2.waitKey(0)
cv2.destroyAllWindows()