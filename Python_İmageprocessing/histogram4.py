import cv2
import matplotlib.pyplot as plt

# Resmi yükle
img = cv2.imread('deneme.jpg')

# Renk kanallarına ayır
r=img[:,:,2]
g=img[:,:,1]
b=img[:,:,0]

#b,g,r=cv2.split(img)
# Histogramları hesapla
hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])

# Histogram grafiklerini çiz
plt.plot(hist_b, color='b')
plt.plot(hist_g, color='g')
plt.plot(hist_r, color='r')
plt.xlabel('Piksel Değeri')
plt.ylabel('Piksel Sayısı')
plt.title('RGB Histogramları')
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
