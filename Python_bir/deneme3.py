import cv2
import numpy as np

# Resmi yükle
img = cv2.imread('deneme.png')

# Resmin boyutunu al
row, col, ch = img.shape

# Gürültü eklemek için yeni bir numpy dizisi oluştur
noisy_img = np.zeros((row, col, ch), np.uint8)

# Rastgele seçilen pikselleri siyah veya beyaz yaparak gürültü eklemek
for i in range(row):
    for j in range(col):
        rdn = np.random.random()
        if rdn < 0.05:
            noisy_img[i][j] = [0, 0, 0]
        elif rdn > 0.95:
            noisy_img[i][j] = [255, 255, 255]
        else:
            noisy_img[i][j] = img[i][j]

# Gürültülü resmi kaydet
cv2.imshow('gurultulu_resim.jpg', noisy_img)
cv2.waitKey(0)
cv2.destroyAllWindows()