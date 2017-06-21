import cv2
import numpy as np

class FaceDetector(object):

    def __init__(self):
        self.faceCascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

    def detectFaces(self, image):
        image = self.preProcessing(image)
        detected = self.faceCascade.detectMultiScale(
            image,
            scaleFactor = 1.25,
            minNeighbors = 3,
            minSize = (20, 20),
            flags = cv2.CASCADE_SCALE_IMAGE
        )
        return detected

    def preProcessing(self, image):
        grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        cl1 = clahe.apply(grey)
        return cl1
