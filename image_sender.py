from time import time

class ImageSender:

    def __init__(self):
        self.frames = []
        files = ['1', '2', '3', '4', '5']
        for f in files:  
           self.frames.append(open('./static/img/' + f + '.jpg', 'rb').read())
    
    def get_frame(self):
        return self.frames[int(time()) % 5]



if __name__=='__main__':
    cam.open_camera()