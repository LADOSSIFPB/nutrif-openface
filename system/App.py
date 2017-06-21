from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import FaceDetector as fd
import FaceRecognizer as fz
app = Flask(__name__)


@app.route("/detect", methods=['GET', 'POST'])
def detectFaces(image):
    detector = fd.FaceDetector()
    return detector.detectFaces(image)

@app.route("/recognize", methods=['GET', 'POST'])
def recognizeFace(face):
    return fz.recognize(face)

if __name__ == "__main__":
    app.run(
    debug=True)
