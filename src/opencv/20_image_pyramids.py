import cv2
import numpy as np

img = cv2.imread('lena.jpg')

cv2.imshow('original', img)
lr1 = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr1)
hr2 = cv2.pyrUp(lr2)
cv2.imshow('lr1', lr1)
cv2.imshow('lr2', lr2)
cv2.imshow('hr2', hr2)

cv2.waitKey(0)
cv2.destroyAllWindows()