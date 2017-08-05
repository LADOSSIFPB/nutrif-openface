import cv2
import numpy as np
import dlib
import openface
import alignDlib
import math
import os
import subprocess

class FaceRecognizer(object):

    def __init__(self):
        self.classifier = "../feature/classifier.pkl"

    def recognize(self, image):
        # python system/classifier.py infer feature/classifier.pkl images/201621230024/IMG_0798.png
        # os.system("python classifier.py infer ../feature/classifier.pkl uploads/" + image)
        path = 'uploads/' + image
        cmd = ['python', 'classifier.py', 'infer', '../feature/classifier.pkl', path]
        output = subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0]
        return output
