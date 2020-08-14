import numpy as np
import cv2
import pyautogui as pgi

codec = cv2.VideoWriter_fourcc(*"XVID")
screenSize = pgi.size()

output = cv2.VideoWriter("screen.avi", codec, 20.0, screenSize)

i = 1000
while i > 0:
    i -= 1
    img = pgi.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output.write(frame)
    # cv2.imshow("Recording", frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# cv2.destroyAllWindows()
output.release()