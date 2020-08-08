import cv2;

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

print(img.shape) #returns a tuple of number of rows, columns and channels
print(img.size) #returns total number of pixels
print(img.dtype) #returns image datatype

b, g, r = cv2.split(img)
#img = cv2.merge((r, g, b))

ball = img[280:340, 330:390]

img[273:333, 100:160] = ball

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

dst = cv2.add(img, img2)
dst2 = cv2.addWeighted(img, 0.9, img2, 0.1, 0)

cv2.imshow('image', img)
cv2.imshow('image2', dst)
cv2.imshow('image3', dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()