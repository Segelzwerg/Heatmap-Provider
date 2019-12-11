from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def hello_world():
    return 'Hello World!'


@app.route('/upload', methods=['GET', 'POST', 'PUT'])
def upload_file():
    r = request
    if request.method == 'PUT':
        # TODO: save body
        return 'file uploaded successfully'
    elif request.method == 'GET':
        return "Please send a gpx file."


if __name__ == '__main__':
    app.run()
