import cv2
import numpy as np

apple = cv2.imread('apple.jpg')
orange = cv2.imread('orange.jpg')
apple_orange = np.hstack((apple[:, :256], orange[:, 254:]))

cv2.imshow('ao', apple_orange)

#generate guassian pyramid for apple
apple_layer = apple.copy()
gp_apple = [apple_layer]
for i in range(6):
    apple_layer = cv2.pyrDown(apple_layer)
    gp_apple.append(apple_layer)

#generate guassian pyramid for orange
orange_layer = orange.copy()
gp_orange = [orange_layer]
for i in range(6):
    orange_layer = cv2.pyrDown(orange_layer)
    gp_orange.append(orange_layer)

#generate laplassian pyramid for apple
apple_layer = gp_apple[5]
lp_apple = [apple_layer]
for i in range(5, 0, -1):
    guassian_extended = cv2.pyrUp(gp_apple[i])
    laplasian = cv2.subtract(gp_apple[i-1], guassian_extended)
    lp_apple.append(laplasian)


#generate laplassian pyramid for orange
orange_layer = gp_orange[5]
lp_orange = [orange_layer]
for i in range(5, 0, -1):
    guassian_extended = cv2.pyrUp(gp_orange[i])
    laplasian = cv2.subtract(gp_orange[i-1], guassian_extended)
    lp_orange.append(laplasian)

apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    cols, rows, channels = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)

#reconstruct image
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, 6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)

cv2.imshow('apple_orange_reconstruct', apple_orange_reconstruct)

cv2.waitKey(0)
cv2.destroyAllWindows()