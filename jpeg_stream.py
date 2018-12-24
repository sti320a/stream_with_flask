from flask import Flask, render_template, Response
# from camera import Camera

# VideoCameraに変更
from camera import VideoCamera 
from time import sleep

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def generate(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/feed')
def feed():
    # VideoCameraに変更 
    return Response(generate(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)