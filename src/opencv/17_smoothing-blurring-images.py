import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('saltandpeppernoise.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernal = np.ones((5,5), np.float)/25
dst = cv2.filter2D(img, -1, kernal) #homogeneous filter
blur = cv2.blur(img, (5, 5))
gblur = cv2.GaussianBlur(img, (5,5), 0)
median = cv2.medianBlur(img, 5)
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['image', '2D Convolution', 'Blur', 'GBlur', 'median', 'bilateral']
images = [img, dst, blur, gblur, median, bilateral]

for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
