import cv2
import numpy as np
img = cv2.imread('lena.jpg', cv2.IMREAD_COLOR)

if type(img) is np.ndarray:
    # cv2.startWindowThread()
    # cv2.namedWindow("lena")
    cv2.imshow('lena', img)
    # cv2.waitKey(2000) #wait for 2 sec before closing window
    k = cv2.waitKey() & 0xFF
    

    if k == 27: # escape key
        cv2.destroyAllWindows()
    elif k == ord('s'):
        cv2.imwrite('lena_copy.png', img)
        cv2.destroyAllWindows()
else:
    print('image not found')