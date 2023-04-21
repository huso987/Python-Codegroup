import cv2
import numpy as np

# Resmi okuyun
img = cv2.imread('deneme.png')

# Görüntüyü ters çevirin
#2^8 -1 =255
img_inverted = 255 - img

# Ters çevrilen görüntüyü gösterin
cv2.imshow('Inverted Image', img_inverted)
cv2.waitKey(0)
cv2.destroyAllWindows()