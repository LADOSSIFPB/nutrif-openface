import cv2
import numpy as np

class FaceDetector(object):

    def __init__(self):
        self.facecascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.detector = dlib.get_frontal_face_detector()

    def detectFaces(self, image):
        image = cv2.imread(image)
        image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
