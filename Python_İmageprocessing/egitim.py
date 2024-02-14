import cv2
import numpy as np
import matplotlib.pyplot as plt

# Resmi yükle
img = cv2.imread('deneme.png', 0)

# Histogramı hesapla
hist, bins = np.histogram(img.flatten(), 256, [0, 256])

# Kumulatif histogramı hesapla
cumulative_hist = np.cumsum(hist)

# Kumulatif histogram grafiği
plt.plot(cumulative_hist)

# Grafik başlığı ve ekseni etiketleri
plt.title('Kumulatif Histogram')
plt.xlabel('Piksel Değerleri')
plt.ylabel('Kümülatif Sayı')

plt.show()