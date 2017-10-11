import cv2
import numpy as np
from optparse import  OptionParser
parser = OptionParser()
parser.add_option("-f","--filename",metavar="FILE",help="the input data",dest="filename")  
(options,args) = parser.parse_args()


img_path = options.filename

# load image
img = cv2.imread(img_path)


# Create Structuring Element
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))




# erode the image

#eroded = cv2.erode(img,kernel)
#cv2.imshow('Erode Image',eroded)

# dilate the image

dilated = cv2.dilate(img, kernel)
cv2.imshow('Dilated Imagea', dilated)


cv2.waitKey(0)

