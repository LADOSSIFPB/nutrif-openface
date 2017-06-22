
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import FaceDetector as fd

app = Flask(__name__)

@app.route("/detect", methods=['POST'])
def detectFaces(image):
    detector = fd.FaceDetector()
    return detector.detectFaces(image)

@app.route("/compare", methods=['POST'])
def compareFaces(image):
    

@app.route("/train", methods=['GET', 'POST'])
def train():
    return ""

if __name__ == "__main__":
    app.run(
    debug=True)
