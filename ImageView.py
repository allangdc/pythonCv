__author__ = 'guest-yyDj9e'

import cv2

class ImageView:
    __image = 0
    __title = "Untitled"

    def setTitle(self, title):
        self.__title = title

    def Title(self):
        return self.__title

    def LoadImage(self, image):
        self.__image = cv2.imread(image)

    def Show(self, time=0):
        cv2.namedWindow(self.__title, cv2.WINDOW_NORMAL)
        cv2.imshow(self.__title, self.__image)
        return cv2.waitKey(time)
