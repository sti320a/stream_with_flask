from time import time

class Camera(object):
    def __init__(self):
        self.frames = []
        self.files = ['1', '2', '3', '4', '5']

        for f in self.files:
            self.frames.append(open('./static/img/' + f + '.jpg', 'rb').read())

    def get_frame(self):
        return self.frames[int(time()) % len(self.files)]

# VideoCameraを追加
class VideoCamera():
    def __init__(self):
        self.frames = []
        self.files = ['1', '2', '3']

        for f in self.files:
            self.frames.append(open('./static/video/' + f + '.avi', 'rb').read())

    def get_frame(self):
        return self.frames[0]


cam = VideoCamera()

if __name__=='__main__':
    cam.open_camera()


# from time import time, sleep
# import cv2

# class Camera():
#     def __init__(self):
#         self.frames = [open('./static/img/img' + num + '.jpg', 'rb').read() for num in ['1', '2', '3', '4', '5', '6', '7']]
        
#     def get_frame(self):
#         # cnt = self.open_camera()
#         # self.frames = [open('./static/img/img' + str(f) + '.jpg', 'rb').read() for f in range(0,7)]
#         return self.frames[int(time()) % 7]
    
#     def open_camera(self):
#         self.cap = cv2.VideoCapture(0)
        
#         cnt = 0

#         while True:
#             path = './static/img/img' + str(cnt) + '.jpg'
#             ret, frame = self.cap.read()
            
#             cv2.imshow('Raw Frame', frame)
#             cv2.imwrite(path, frame)

#             cnt += 1

#             k = cv2.waitKey(1)
#             if k == 27:
#                 break
            
#             if cnt == 10:
#                 break

#             sleep(1)

#         self.cap.release()
#         cv2.destroyAllWindows()

#         return cnt    

