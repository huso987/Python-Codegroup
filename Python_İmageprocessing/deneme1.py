import cv2

# Resmi yükle
img = cv2.imread('deneme.png')
img1= cv2.imread('denme.png')

bright_img = cv2.add(img1, -img)

#İki fotoğrafı birbirinden çıkarma
cv2.imshow('Orijinal Resim 1', img1)
cv2.imshow('Orijinal Resim', img)
cv2.imshow('Çıkarma İşeminden sonraki resim', bright_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
