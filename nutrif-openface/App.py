from flask import Flask, render_template, request, jsonify
import FaceDetector as fd
import FaceRecognizer as fz
import base64
import os

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

def upload(image):
    if image and allowed_file(image.filename):
        f = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(f)
    else:
        return 'not received'

@app.route('/', methods=['GET', 'POST'])
def index():
    return 'routes: <i>/detect</i> and <i>/recognize</i>'

@app.route('/detect', methods=['POST'])
def detect_faces():
    if request.is_json:
        data = request.get_json()
        img64 = data['image']
        imgdata = base64.decodestring(img64)
        imgfile = 'uploads/detectface.png'
        with open(imgfile, 'wb') as f:
            f.write(imgdata)
        detector = fd.FaceDetector()
        faces = detector.detect_faces(imgfile)
        return jsonify(faces = str(faces))
    else:
        return 'Json not received'

@app.route('/recognize', methods=['GET', 'POST'])
def recognize_face():
    if request.is_json:
        match = False
        data = request.get_json()
        id_infer = data['id']
        img64 = data['image']
        imgdata = base64.decodestring(img64)
        img_file = 'uploads/face.png'
        with open(img_file, 'wb') as f:
            f.write(imgdata)

        recognizer = fz.FaceRecognizer()
        person, confidence = recognizer.recognize_face(img_file)
        if person == id_infer:
            match = True

        return jsonify(person = person.decode('utf-8'), confidence = "{:.2f}".format(confidence), match = match)
    else:
        return 'Json not received'

if __name__ == "__main__":
    app.run(
        debug = True, 
        host = '0.0.0.0'
    )
