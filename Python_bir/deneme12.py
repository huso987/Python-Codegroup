import cv2

# Görüntüyü yükle
img = cv2.imread('deneme.png', cv2.IMREAD_GRAYSCALE)

# Eşik değerini belirle
threshold_value = 150
#binary eşik

# Görüntüyü eşikle
ret, thresholded_img = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)

# Eşiklenmiş görüntüyü göster
cv2.imshow('Thresholded Image', thresholded_img)
cv2.waitKey(0)
cv2.destroyAllWindows()