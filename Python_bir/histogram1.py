
import cv2
import matplotlib.pyplot as plt

# histogram hesapama ama fonksiyon ile
img=cv2.imread('deneme.jpg',0)

hist=cv2.calcHist([img],[0],None,[256],[0,256])

plt.plot(hist)
plt.title("histogram")
plt.xlabel("pixel degerleri")
plt.ylabel("pixel sayısı")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()