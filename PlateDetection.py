__author__ = 'guest-yyDj9e'

import ImageView as iv
import cv2

class PlateDetection(iv.ImageView):

    def __init__(self):
        print "Initied PlateDetection"

    def __Gray(self):
        img = cv2.cvtColor(self.Image(), cv2.COLOR_BGR2GRAY)
        self.setImage(img)

    def __Blur(self):
        img = cv2.blur(self.Image(), (5,5))
        self.setImage(img)

    def __Sobel(self):
        img = cv2.Sobel(self.Image(), cv2.CV_8U, 1, 0, None, 3, 1, 0)
        self.setImage(img)

    def __Threshold(self):
        ret, img = cv2.threshold(self.Image(), 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
        self.setImage(img)

    def Segmentation(self):
        self.__Gray()
        self.__Blur()
        self.__Sobel()
        self.__Threshold()

