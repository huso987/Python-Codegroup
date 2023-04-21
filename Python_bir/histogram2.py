import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('deneme.jpg')
# histogram hesaplama ama for döngüsü ile
histsize=256
histrange=(0,256)
hist=np.zeros(histsize, dtype=np.int)

for pixelval in img.ravel():
    hist[pixelval] += 1


plt.plot(hist)
plt.title("histogram")
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()