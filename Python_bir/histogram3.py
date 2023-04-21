import cv2
import numpy as np
import matplotlib.pyplot as plt

# Resmi yükleyin (32 bit derinliğiyle)
img = cv2.imread('deneme1.jpg')

# Histogram aralıklarını belirleyin
bins = np.linspace(0, 2**32, num=256)

# Histogramı hesaplayın
hist, edges = np.histogram(img.ravel(), bins=bins)

# Histogram grafiğini çizin
plt.bar(edges[:-1], hist, width=np.diff(edges), align='edge')
plt.xlabel('Piksel Değeri')
plt.ylabel('Piksel Sayısı')
plt.title('32 Bitlik Resmin Histogramı')

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()