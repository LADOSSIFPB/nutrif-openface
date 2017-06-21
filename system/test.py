import FaceDetector
import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument('image', type=str, help="image to detect faces")
args = parser.parse_args()

dir = args.image
image = cv2.imread(dir)
detector = FaceDetector.FaceDetector()
faces = detector.detectFaces(image)
print "Found {0} faces!".format(len(faces))
