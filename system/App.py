from flask import Flask, render_template, request
import FaceDetector as fd
import FaceRecognizer as fz
import base64
import os

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg'])

def allowedFile(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

def upload(image):
    if image and allowedFile(image.filename):
        f = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(f)
    else:
        print('======== ERROR ========')
        return 'not received'

@app.route('/detect', methods=['POST'])
def detectFaces():
    image = request.files['image']
    upload(image)
    detector = fd.FaceDetector()
    faces = detector.detectFaces('uploads/' + image.filename)
    return(str(faces))

# @app.route("/train", methods=['GET'])
# def train():
#     recognizer = fz.FaceRecognizer()
#     return recognizer.train()

@app.route("/recognize", methods=['GET', 'POST'])
def recognize():
    if request.method == 'POST':
        face = request.files['face']
        upload(face)
        recognizer = fz.FaceRecognizer()
        return recognizer.recognize(face.filename)
    
    return False


if __name__ == "__main__":
    app.run(
        debug = True, 
        host = '0.0.0.0'
    )
