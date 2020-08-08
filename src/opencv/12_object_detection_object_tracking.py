import cv2
import numpy as np

def onTrackbarChange(x):
    pass

cv2.namedWindow('Tracking')
cv2.createTrackbar('LH', 'Tracking', 0, 255, onTrackbarChange)
cv2.createTrackbar('LS', 'Tracking', 0, 255, onTrackbarChange)
cv2.createTrackbar('LV', 'Tracking', 0, 255, onTrackbarChange)
cv2.createTrackbar('UH', 'Tracking', 255, 255, onTrackbarChange)
cv2.createTrackbar('US', 'Tracking', 255, 255, onTrackbarChange)
cv2.createTrackbar('UV', 'Tracking', 255, 255, onTrackbarChange)

while True:
    frame = cv2.imread('smarties.png')
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_blue = np.array([cv2.getTrackbarPos('LH', 'Tracking'), cv2.getTrackbarPos('LS', 'Tracking'), cv2.getTrackbarPos('LV', 'Tracking')])
    u_blue = np.array([cv2.getTrackbarPos('UH', 'Tracking'), cv2.getTrackbarPos('US', 'Tracking'), cv2.getTrackbarPos('UV', 'Tracking')])
    mask = cv2.inRange(hsv, l_blue, u_blue)
    res = cv2.bitwise_and(frame, frame,mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)


    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break

cv2.destroyAllWindows()