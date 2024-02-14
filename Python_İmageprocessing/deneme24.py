import cv2
import numpy as np

# Resmi oku
img = cv2.imread('deneme.png', cv2.IMREAD_GRAYSCALE)

# Filtre boyutlarını tanımla
filter_sizes = [3, 5, 21]

# Her bir boyuttaki filtre için ortalama filtre uygula ve sonuçları göster
for size in filter_sizes:
    # Filtreyi tanımla
    kernel = np.ones((size, size), np.float32) / (size ** 2)
    # Filtreyi resme uygula
    filtered_img = cv2.filter2D(img, -1, kernel)
    # Resimleri göster
    cv2.imshow(f'Filtered Image ({size}x{size})', filtered_img)

# Çıkış yapmak için bir tuşa basılmasını bekle
cv2.waitKey(0)
cv2.destroyAllWindows()