import cv2
import numpy as np

img1 = np.zeros((250, 500, 3), np.uint8)
cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = cv2.imread('messi5.jpg')

img2 = cv2.resize(img2, (250, 500))


cv2.imshow('img1', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()