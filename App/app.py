import os
import shutil

from flask import Flask, request, send_file
from werkzeug.utils import secure_filename

from App.heatmap_service import heatmap_service

app = Flask(__name__)

session = 0


def create_app():
    return app;


def test_client():
    app.testing = True

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
        session_id = request.form['session']

        # creates user folder
        upload_directory = os.path.join(app.instance_path, session_id)
        os.makedirs(upload_directory, exist_ok=True)

        file.save(os.path.join(upload_directory, secure_filename(file.filename)))
        print("Uploaded a file for session: " + str(session_id))
        return 'file uploaded successfully'
    elif request.method == 'GET':
        return "Please send a gpx file and session id."


@app.route('/generate', methods=['POST'])
def generate():
    if request.method == 'POST':
        session_id = request.form['session']

        return heatmap_service(app.instance_path, session_id)
    return "Failed to generate."


@app.route("/get-image", methods=['POST'])
def get_image():
    if request.method == 'POST':
        session_id = request.form['session']
        path = os.path.dirname(app.instance_path)
        file_name = os.path.join(path, str(session_id) + ".png")
        if os.path.isfile(file_name):
            print("Send image for session: " + str(session_id))
            return send_file(file_name, mimetype='image/png')
        return "Response not done yet, make sure you you started the generation process by sending a get request to " \
               "/generate with your session id. "
    return "Could not retrieve image."


if __name__ == '__main__':
    dirname = app.instance_path
    try:
        shutil.rmtree(dirname)
    except Exception as e:
        print(e)
        print("Already clean instance.")
    print("Heatmap Provider is online.")
    app.run()
