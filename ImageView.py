__author__ = 'guest-yyDj9e'

import cv2
import numpy as np

class ImageView:
    __image = 0
    __title = "Untitled"

    def __init__(self, image=0):
        self.setImage(image)
        print "Initied ImageView"

    def setTitle(self, title):
        self.__title = title

    def Title(self):
        return self.__title

    def setImage(self, image):
        if isinstance(image, str):
            print "LoadImage() = string"
            self.__image = cv2.imread(image)
            self.setTitle(image)
        elif isinstance(image, np.ndarray):
            print "LoadImage() = np.ndarray"
            self.__image = image
        else:
            print "LoadImage() = Other"

    def Image(self):
        return self.__image

    def Show(self, time=0, windowType = cv2.WINDOW_NORMAL):
        cv2.namedWindow(self.__title, windowType)
        cv2.imshow(self.__title, self.__image)
        return cv2.waitKey(time)
