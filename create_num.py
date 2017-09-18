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

def CombineImage(blank,element):
    for i in range(len(element)):
        blank[:height , i*width:(i+1) * width ,:3] = cv2.imread(element[i]+'.jpg')
    cv2.imshow('all',blank)
    return blank

def ClearCombineImage(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # change the image to gray image
    ret,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY) # change the image to black and write

    _ , contours, hierarchy  =  cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img,contours,-1,(0,0,255),3)  
    cv2.imshow("img", img)  
    cv2.waitKey(0)  




n = GetRandNum(number)
print(n)

blankimg = Create_blank(width * number , height)

cv2.imshow("all",blankimg)
img = CombineImage(blankimg,n)

#ClearCombineImage(img)
cv2.waitKey(0) 

	
	



