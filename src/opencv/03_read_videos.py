import cv2
import numpy as np
cap = cv2.VideoCapture(0) #default camera 0,
fourcc = cv2.VideoWriter_fourcc(*'XVID') #visit fourcc website for code list
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
print(cap.isOpened())
while(True):
    ret, frame = cap.read()
    if ret:
        wd = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        ht = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(frame)

        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()


