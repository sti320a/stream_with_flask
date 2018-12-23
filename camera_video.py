import cv2
import sys
import os
from time import time, sleep
from datetime import datetime



d = datetime.now()
filename = str(d)[21:26] + '.avi'

cap = cv2.VideoCapture(0)
fps = 15

# 3:CV_CAP_PROP_FRAME_WIDTH  4:CV_CAP_PROP_FRAME_HEIGHT
size = (int(cap.get(3)),int(cap.get(4)))
writer = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('D', 'I', 'V', 'X'), fps, size)

start = time()
while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        cv2.imshow('frame', frame)

        frame = cv2.resize(frame, (640, 480))
        writer.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        end  = time()
        if end - start >= 10:
            break

    else:
        break

sleep(2)
cap.release()
writer.release()


os.rename('output.avi','%s' % (filename))

cv2.destroyAllWindows()
