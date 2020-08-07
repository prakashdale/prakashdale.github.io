import cv2

img = cv2.imread('lena.jpg', cv2.IMREAD_COLOR)

img = cv2.line(img, (0,0), (255, 255), (0, 200, 0), 1)
img = cv2.putText(img, "Hello OpenCV", (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.imshow('lena', img)
cv2.waitKey(0)
cv2.destroyAllWindows()