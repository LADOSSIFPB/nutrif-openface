import cv2
import numpy as np

class FaceDetector(object):

    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

    def detect_faces(self, image):
        img = cv2.imread(image)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        return len(faces)
