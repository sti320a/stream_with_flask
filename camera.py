from time import time, sleep
import cv2

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
        self.files = []
        self.MAX_FRAME_NUM = 20 # 撮影枚数を指定
        self.RECORD_INTERVAL = 0.5 # 撮影のインターバルを指定

        target=self.record()
        
    def get_frame(self):
        # 撮影された画像を順に返す
        for file in self.files:
            self.frames.append(open(file, 'rb').read())
        return self.frames[int(time()) % len(self.frames)]

    def record(self):
        self.cap = cv2.VideoCapture(0)
        
        cnt = 0
        while True:
            # 撮影したファイルの保存先を指定
            path = './static/img/img' + str(cnt) + '.jpg'
            ret, frame = self.cap.read()
            self.files.append(path)

            cv2.imwrite(path, frame)

            # ESCキーで停止する
            k = cv2.waitKey(1)
            if k == 27:
                break
            
            # 指定した枚数以上を撮影したら停止する
            cnt += 1
            if cnt == self.MAX_FRAME_NUM:
                break

            # 撮影のインターバルを指定
            sleep(self.RECORD_INTERVAL)
            
        self.cap.release()
        cv2.destroyAllWindows()


# if __name__=='__main__':
#     cam.open_camera()


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

