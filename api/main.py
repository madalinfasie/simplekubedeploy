import os
from posixpath import dirname

import flask


app = flask.Flask(__name__)

FILE_PATH = '/data/resources/counter'


def _count(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            counter = int(f.read()) + 1
    else:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        counter = 1

    with open(filepath, 'w') as f:
        f.write(str(counter))

    return counter


@app.route('/')
def index():
    return flask.Response(f'<h1>Saw your face {_count(FILE_PATH)} times</h1>')


if __name__ == '__main__':
    app.run()