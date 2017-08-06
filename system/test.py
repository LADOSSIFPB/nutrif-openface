# # import FaceDetector
# # import argparse
# # import cv2
# #
# # parser = argparse.ArgumentParser()
# # parser.add_argument('image', type=str, help="image to detect faces")
# # args = parser.parse_args()
# #
# # dir = args.image
# # image = cv2.imread(dir)
# # detector = FaceDetector.FaceDetector()
# # faces = detector.detectFaces(image)
# # print(len(faces))
# # print "Found {0} faces!".format(len(faces))
# import cv2
# import sys

# # Get user supplied values
# imagePath = sys.argv[1]
# cascPath = "cascades/haarcascade_frontalface_default.xml"

# # Create the haar cascade
# faceCascade = cv2.CascadeClassifier(cascPath)

# # Read the image
# image = cv2.imread(imagePath)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Detect faces in the image
# faces = faceCascade.detectMultiScale(
#     gray,
#     scaleFactor=1.1,
#     minNeighbors=5,
#     minSize=(30, 30),
#     flags = cv2.cv.CV_HAAR_SCALE_IMAGE
# )

# print("Found {0} faces!".format(len(faces)))

# # Draw a rectangle around the faces
# for (x, y, w, h) in faces:
#     cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# cv2.imshow("Faces found", image)
# cv2.waitKey(0)

# import base64

# with open("IMG_0320.png", "rb") as image_file:
#     encoded_string = base64.encodestring(image_file.read())
 
# encoded_string = encoded_string.decode('utf-8').replace('\n', '')

# with open('test.txt', 'w') as file:
#     file.write(encoded_string)
