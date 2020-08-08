import cv2
import numpy as np

img1 = np.zeros((250, 500, 3), np.uint8)
cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = cv2.imread('messi5.jpg')

img2 = cv2.resize(img2, (500, 250))


cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('bitwizeand', cv2.bitwise_and(img1, img2))
cv2.imshow('bitwizeor', cv2.bitwise_or(img1, img2))
cv2.imshow('bitwizexor', cv2.bitwise_xor(img1, img2))
cv2.imshow('bitwizenot', cv2.bitwise_not(img2))

cv2.waitKey(0)
cv2.destroyAllWindows()