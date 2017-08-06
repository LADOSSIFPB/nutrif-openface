import cv2
import numpy as np

class FaceDetector(object):

    def __init__(self):
        self.faceCascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

    def detectFaces(self, image):
        img = cv2.imread(image)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.faceCascade.detectMultiScale(gray, 1.3, 5)
        return len(faces)
