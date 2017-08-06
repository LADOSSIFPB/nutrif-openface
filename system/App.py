from flask import Flask, render_template, request, jsonify
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

@app.route('/recognize', methods=['GET', 'POST'])
def recognize():
    if request.is_json:
        data = request.get_json()
        img64 = data['image']
        imgdata = base64.decodestring(img64)
        imgfile = 'uploads/face.png'
        with open(imgfile, 'wb') as f:
            f.write(imgdata)

        recognizer = fz.FaceRecognizer()
        person, confidence = recognizer.recognizeFace(imgfile)
        return jsonify(person = person.decode('utf-8'), confidence = "{:.2f}".format(confidence))
    else:
        return 'Json not received'

if __name__ == "__main__":
    app.run(
        debug = True, 
        host = '0.0.0.0'
    )
