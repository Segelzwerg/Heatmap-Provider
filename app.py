import os

from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def hello_world():
    return 'Hello World!'


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        upload_directory = request.form['session']

        # creates user folder
        upload_directory = os.path.join(app.instance_path, upload_directory)
        os.makedirs(upload_directory, exist_ok=True)

        file.save(os.path.join(upload_directory, secure_filename(file.name)))
        return 'file uploaded successfully'
    elif request.method == 'GET':
        return "Please send a gpx file and session id."


if __name__ == '__main__':
    app.run()
