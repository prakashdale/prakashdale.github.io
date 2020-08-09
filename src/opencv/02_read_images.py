import cv2
import numpy as np
img = cv2.imread('lena.jpg', cv2.IMREAD_COLOR)

if type(img) is np.ndarray:
    cv2.imshow('lena', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27: # escape key
        cv2.destroyAllWindows()
    elif k == ord('s'):
        # Save image as lena_copy.png
        cv2.imwrite('lena_copy.png', img)
        cv2.destroyAllWindows()
else:
    print('image not found')