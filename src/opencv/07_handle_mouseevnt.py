import numpy as np
import cv2

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ' ', y)
        cv2.putText(img, str(x) + ', ' + str(y), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,255), 1, 2 )
        cv2.imshow('image', img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        msg = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, msg, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1, 2)
        cv2.imshow('image', img)

#img = np.zeros((1024, 1024, 3), np.uint8)
img = cv2.imread('lena.jpg')
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()