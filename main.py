__author__ = 'guest-yyDj9e'

#import ImageView as iv
import PlateDetection as pd
import cv2

def main():
    FILE = "/tmp/guest-yyDj9e/Pictures/car01.jpg"
    img = pd.PlateDetection()
    img.setImage(FILE)
    img.Segmentation()
    img.Show()
    print "FIM"


if __name__ == '__main__':
    main()