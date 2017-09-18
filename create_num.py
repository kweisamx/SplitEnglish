import cv2
import numpy as np
from random import randint

#CONST
height = 130
width = 65
number = 4


def Create_blank(width, height, rgb_color=(0, 0, 0)):
	"""Create new image(numpy array) filled with certain color in RGB"""
	# Create black blank image
	image = np.zeros((height, width, 3), np.uint8)

	# Since OpenCV uses BGR, convert the color first
	color = tuple(reversed(rgb_color))
	# Fill image with color
	image[:] = color

	return image

def GetRandNum(nunber):
    randnum = []
    for i in range(number):
	    randnum.append(str(randint(0,9)))
    return randnum

def GetImage(element):
    for i in range(len(element)):
        e = cv2.imread(element[i]+'.jpg')
        cv2.imshow(element[i],e)
def CombineImage(blank,element):
    for i in range(len(element)):
        blank[:height , i*width:(i+1) * width ,:3] = cv2.imread(element[i]+'.jpg')
    cv2.imshow('all',blank)
n = GetRandNum(number)
print(n)

blankimg = Create_blank(width * number , height)

cv2.imshow("all",blankimg)
#GetImage(n)
CombineImage(blankimg,n)
cv2.waitKey(0) 

	
	



