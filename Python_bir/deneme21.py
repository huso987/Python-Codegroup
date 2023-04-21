import cv2

# Görüntü yükleme
img = cv2.imread('huso2.jpg')

# 5x5 boyutunda ortalama filtresi
kernel = (21, 21)
blur_img = cv2.blur(img, kernel)

# Sonuçları gösterme
cv2.imshow('Orjinal Görüntü', img)
cv2.imshow('Ortalama Filtresi Uygulanmış Görüntü', blur_img)
cv2.waitKey(0)
cv2.destroyAllWindows()