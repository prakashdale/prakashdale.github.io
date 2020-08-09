import cv2
import numpy as np
from matplotlib import pyplot as plt
def onTrackbarChange(x):
    pass
cv2.namedWindow('tb')
cv2.createTrackbar('th1', 'tb', 100, 255, onTrackbarChange)
cv2.createTrackbar('th2', 'tb', 200, 255, onTrackbarChange)



img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)


while(True):
    th1 = cv2.getTrackbarPos('th1', 'tb')
    th2 = cv2.getTrackbarPos('th2', 'tb')
    canny = cv2.Canny(img, th1, th2)
    cv2.imshow('img', img)
    cv2.imshow('canny', canny)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    

    
    
    


cv2.destroyAllWindows()