import cv2
import numpy as np
import openface

np.set_printoptions(precision=2)

class FaceCompare(object):

    def __init__(self):
        self.imgDim = 96
        self.align = openface.AlignDlib("../models/dlib/shape_predictor_68_face_landmarks.dat")
        self.net = openface.TorchNeuralNet("../models/openface/nn4.small2.v1.t7", imgDim)

    def compare(image, id):
        # implementar media de comparacao com repositorio

    def getRep(image):
        image = cv2.imread(image)
        if image is None:
            raise Exception("Unable to load image: {}".format(imgPath))
        imageRgb = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
         bb = align.getLargestFaceBoundingBox(rgbImg)
        alignedFace = align.align(self.imgDim, imageRgb, bb,
                             landmarkIndices = openface.AlignDlib.OUTER_EYES_AND_NOSE)
        if alignedFace is None:
            raise Exception("Unable to align image: {}".format(image))
        rep = net.foward(alignedFace)
        return rep
