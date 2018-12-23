import cv2
import sys
import os
from time import time, sleep
from datetime import datetime


class VideoCamera():
    def __init__(self):
        #self.frames = [open('./static/img/video' + num + '.avi', 'rb').read() for num in ['1', '2', '3', '4', '5', '6', '7']]
        pass

    def get_frame(self):
        return self.frames[int(time()) % 7]

    def open_camera(self):

        self.cap = cv2.VideoCapture(0)
        size = (int(self.cap.get(3)),int(self.cap.get(4)))

        fps = 20
        start = time()

        for i in range(0, 3):
            path = './static/img/video' + str(i) + '.avi'
            writer = cv2.VideoWriter(path, cv2.VideoWriter_fourcc('D', 'I', 'V', 'X'), fps, size)

            start = time()

            while True:
                ret, frame = self.cap.read()
                cv2.imshow('frame', frame)

                frame = cv2.resize(frame, (640, 480))
                writer.write(frame)

                end = time()

                if int(end - start) >= 5:
                    writer.release()
                    break

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break


        self.cap.release()

        cv2.destroyAllWindows()


cam = VideoCamera()

if __name__=='__main__':
    cam.open_camera()