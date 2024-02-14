import cv2
import numpy as np
import matplotlib.pyplot as plt
#normal resimden noisy olan resim çıkartınca noisy miktarı çıkar
peppers = cv2.imread('deneme.png')
noisy_peppers = np.uint8(np.clip(peppers + 25 * np.random.randn(*peppers.shape), 0, 255))
diff_img = cv2.absdiff(peppers, noisy_peppers)

plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1), plt.imshow(cv2.cvtColor(peppers, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(1, 3, 2), plt.imshow(cv2.cvtColor(noisy_peppers, cv2.COLOR_BGR2RGB)), plt.title('Noisy Image')
plt.subplot(1, 3, 3), plt.imshow(cv2.cvtColor(diff_img, cv2.COLOR_BGR2RGB)), plt.title('Absolute Difference')
plt.show()
