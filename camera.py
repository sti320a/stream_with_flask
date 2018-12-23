from time import time

class Camera(object):
    def __init__(self):
        self.frames = [open('./static/img/' + f + '.jpg', 'rb').read() for f in ['1', '2', '3', '4', '5', '6', '7']]

    def get_frame(self):
        return self.frames[int(time()) % 7]