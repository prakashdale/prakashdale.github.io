import numpy as np
import cv2

img = cv2.imread('shapes.jpg', cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (255,0,0), 2)
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if len(approx) ==3:        
        cv2.putText(img, 'Triangle', (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))    
    elif len(approx) == 4:        
        cv2.putText(img, 'Rectable', (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
    elif len(approx) == 5:    
        cv2.putText(img, 'Pentagon', (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
    elif len(approx) == 12:
        cv2.putText(img, 'Star', (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
    else:
        cv2.putText(img, 'Shape', (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
    
cv2.imshow('image', thresh)
cv2.imshow('contours', img)

cv2.waitKey(0)
cv2.destroyAllWindows()