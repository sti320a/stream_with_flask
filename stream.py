# stream.py
from flask import Flask, Response, render_template, stream_with_context
from time import sleep

app = Flask(__name__)


def stream_template(template_name, **context):
    app.update_template_context(context)
    t = app.jinja_env.get_template(template_name)
    rv = t.stream(context)
    rv.enable_buffering(3)
    return rv

def iter_all_rows():
    i = 0
    while True:
        yield str(i)
        i += 1
        sleep(1)


@app.route('/')
def render_large_template():
    rows = iter_all_rows()
    return Response(stream_with_context(stream_template('gen.html', rows=rows)))


if __name__=="__main__":
    app.run(debug=True)