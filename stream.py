# stream.py
from flask import Flask, Response, render_template
from time import sleep

app = Flask(__name__)

@app.route('/')
def gen_num_view():
    def generate():
        for num in range(0, 10):
            yield 'hello' + str(num)
            sleep(3)
        # yield render_template('gen.html', num='bbb')
        # yield render_template('gen.html', num='ccc')
        # yield render_template('gen.html', num='ddd')
        # yield render_template('gen.html')
    return Response(generate(), mimetype='text/html')

if __name__=="__main__":
    app.run(debug=True)