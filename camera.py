# from time import time

# class Camera(object):
#     def __init__(self):
#         self.frames = [open('./static/img/' + f + '.jpg', 'rb').read() for f in ['1', '2', '3', '4', '5', '6', '7']]

#     def get_frame(self):
#         return self.frames[int(time()) % 7]

from time import time
import cv2

class Camera():    
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
    
    def get_frame(self):
        return self.frames[int(time()) % 7]
    
    def open_camera(self):
        while True:
            ret, frame = self.cap.read()
            cv2.imshow('Raw Frame', frame)
            k = cv2.waitKey(1)
            if k == 27:
                break
        self.cap.release()
        cv2.destroyAllWindows()
    

cam = Camera()

if __name__=='__main__':
    cam.open_camera()