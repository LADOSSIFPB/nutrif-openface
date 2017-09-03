import os
import math
import subprocess
from operator import itemgetter
import pandas as pd
import cv2
import numpy as np
import dlib
import openface
import alignDlib
import pickle

fileDir = os.path.dirname(os.path.realpath(__file__))
modelsDir = os.path.join(fileDir, '..', 'models')
dlibFacePredictor = os.path.join(modelsDir, 'dlib', 'shape_predictor_68_face_landmarks.dat')
networkModel = os.path.join(modelsDir, 'openface', 'nn4.small2.v1.t7' )
classifier = os.path.join(fileDir, '..', 'feature', 'classifier.pkl')

class FaceRecognizer(object):
    """ Class responsible for train and recognize faces using models and classifier 
    from feature/ and models/ directory   
    """

    def __init__(self):
        self.align = openface.AlignDlib(dlibFacePredictor)
        self.net = openface.TorchNeuralNet(networkModel, 96, False)
        with open(classifier, 'rb') as f: # le = labels, clf = classifier
            (self.le, self.clf) = pickle.load(f) 
    
    def get_rep(self, img):
        bgrImg = cv2.imread(img)
        if bgrImg is None:
            raise Exception("Unable to load image")

        rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)
        face = self.align.getLargestFaceBoundingBox(rgbImg)
        alignedFace = self.align.align(
            96,
            rgbImg,
            face,
            landmarkIndices = openface.AlignDlib.OUTER_EYES_AND_NOSE
        )

        if alignedFace is None:
            raise Exception("Unable to align image")
        
        rep = self.net.forward(alignedFace) 
        return rep
        
    def recognize_face(self, img):
        if self.get_rep(img) is None:
            raise Exception("Could not get 128 measurements")
        r = self.get_rep(img)
        rep = r.reshape(1, -1) #reshape the image array to a single line instead of 2 dimensionals
        prediction = self.clf.predict_proba(rep).ravel()
        maxI = np.argmax(prediction)
        person = self.le.inverse_transform(maxI)
        confidence = prediction[maxI]
        
        return person.decode('utf-8'), confidence        