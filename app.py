import argparse
import os

import strava_local_heatmap
from flask import Flask, request, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)

session = 0


@app.route('/')
@app.route('/index')
def hello_world():
    return 'Hello World!'


@app.route("/create-session", methods=['GET'])
def create_session():
    global session
    session = session + 1
    return str(session)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        upload_directory = request.form['session']

        # creates user folder
        upload_directory = os.path.join(app.instance_path, upload_directory)
        os.makedirs(upload_directory, exist_ok=True)

        file.save(os.path.join(upload_directory, secure_filename(file.filename)))
        return 'file uploaded successfully'
    elif request.method == 'GET':
        return "Please send a gpx file and session id."


@app.route('/generate', methods=['GET'])
def generate():
    if request.method == 'GET':
        session_id = request.form['session']

        # param dir
        dir = os.path.join(app.instance_path, session_id)

        # param file - the filename
        file = str(session_id)

        # setup default values
        bound = [-90, 90, -180, 180]
        csv = False
        glob = '*.gpx'
        nocdist = False
        sigma = 1
        year = 'all'
        zoom = 10

        parser = argparse.ArgumentParser()
        parser.add_argument('--dir', default=dir)
        parser.add_argument('--file', default=file)
        parser.add_argument('--bound', default=bound)
        parser.add_argument('--csv', default=csv)
        parser.add_argument('--glob', default=glob)
        parser.add_argument('--nocdist', default=nocdist)
        parser.add_argument('--sigma', default=sigma)
        parser.add_argument('--year', default=year)
        parser.add_argument('--zoom', default=zoom)

        args = parser.parse_args()

        strava_local_heatmap.main(args)
        return "Generated"
    return "Failed to generate."


@app.route("/get-image", methods=['GET'])
def get_image():
    if request.method == 'GET':
        session_id = request.form['session']
        path = os.path.dirname(app.instance_path)
        file_name = os.path.join(path, str(session_id) + ".png")
        return send_file(file_name, mimetype='image/png')

if __name__ == '__main__':
    app.run()
