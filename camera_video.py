import cv2
import sys
import os
from time import time

d = datetime.datetime.now().isoformat()
filename = str(d) + '.avi'

cap = cv2.VideoCapture(0)
fps = 30

size = (int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
writer = cv2.VideoWriter('output.avi', cv2.cv.CV_FOURCC('D', 'I', 'V', 'X'), fps, size)

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

os.rename('output.avi','%s'%(filename))

cap.release()
writer.release()
cv2.destroyAllWindows()
