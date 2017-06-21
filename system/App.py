from flask import Flask, render_template
from flask_cors import CORS
from JsonUtils import convert_input_to, json_repr
from flask_socketio import SocketIO, emit
import FaceDetector as fd
from Aluno import Aluno

app = Flask(__name__)
CORS(app)

@app.route("/detect", methods=['POST'])
@convert_input_to(Aluno)
def detectFaces(aluno):

    # Recuperar Imagem
    print("mat:" + aluno.matricula)
    #print("imagem:" + aluno.imagem)

    # detector = fd.FaceDetector()
    # return detector.detectFaces(image)

    return "{'retorno':'true'}", 200


@app.route("/train", methods=['GET', 'POST'])
def train():
    return ""

if __name__ == "__main__":
    app.run(
    debug=True)
