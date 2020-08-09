import numpy as np
import cv2

img = cv2.imread('opencv-logo-white.png')
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imggray, 100, 255, 0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print('No of contours', str(len(contours)))

cv2.drawContours(img, contours, -1, (255, 255, 0), 3)

cv2.imshow('img', img)
cv2.imshow('imggray', imggray)

cv2.waitKey(0)
cv2.destroyAllWindows()