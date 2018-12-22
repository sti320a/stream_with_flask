# stream.py

from flask import Flask, Response, render_template

app = Flask(__name__)

def gen_num():
    # for num in range(0, 10):
    #     yield render_template('gen.html', num=num)
    yield render_template('gen.html', num='aaa')
    yield render_template('gen.html', num='bbb')
    yield render_template('gen.html', num='ccc')
    yield render_template('gen.html', num='ddd')
    yield render_template('gen.html', num='eee')

@app.route('/')
def gen_num_view():
    return Response(gen_num())

if __name__=="__main__":
    app.run(debug=True)