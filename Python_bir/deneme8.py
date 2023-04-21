import cv2
import numpy as np
import matplotlib.pyplot as plt

# Resmi yükle
img = cv2.imread('deneme.png')

# Logaritmik dönüşüm parametresi
c = 2

# Resmi double formatına dönüştür
img_double = np.double(img)

# Logaritmik dönüşüm
log_transformed = c * np.log(1 + img_double)

# Ölçekleme (0-255)
log_transformed = np.uint8(255*log_transformed/log_transformed.max())

# Sonuçları görselleştirme
plt.subplot(121),plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Orijinal Resim'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(cv2.cvtColor(log_transformed, cv2.COLOR_BGR2RGB))
plt.title('Logaritmik Dönüşüm'), plt.xticks([]), plt.yticks([])
plt.show()