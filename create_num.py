import cv2
import numpy as np
from random import randint

#CONST
height = 107
width = 57
number = 3
english_num= 3
english_map = dict(zip((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25),('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')))

def Create_blank(width, height, rgb_color=(255, 255, 255)):
    """Create new image(numpy array) filled with certain color in RGB"""
    # Create black blank image
    image = np.zeros((height, width, 3), np.uint8)

    # Since OpenCV uses BGR, convert the color first
    color = tuple(reversed(rgb_color))
    # Fill image with color
    image[:] = color

    return image

def GetRandNum(nunber,digist=True):
    randnum = []
    if digist:
        for i in range(number):
            randnum.append(str(randint(0,9)))
        return randnum
    #english
    else:
        for i in range(number):
            randnum.append(english_map[randint(0,25)])
        return randnum



def CombineImage(blank,element,name):
    for i in range(len(element)):
        element_img = cv2.imread(element[i]+'.jpg')
        h1,w1,_ = element_img.shape
        blank[:h1 , i*w1:(i+1) * w1 ,:3] = element_img
    cv2.imshow(name,blank)
    return blank

def CombineTwoImage(img1,img2):
    h1,w1,_ = img1.shape
    h2,w2,_ = img2.shape
    blank_image =  Create_blank(w1+w2,h1)
    blank_image[:h1,:w1,:3] = img1
    blank_image[:h2,w1:w1+w2,:3] = img2
    cv2.imshow("CombineTwo",blank_image)
    return blank_image

def ClearCombineImage(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # change the image to gray image
    ret,binary = cv2.threshold(gray,200,255,cv2.THRESH_BINARY) # change the image to black and write

    _ , contours, hierarchy  =  cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img,contours,-1,(0,0,0),1)  
    cv2.imshow("img", img)  
    cv2.waitKey(0)  




n = GetRandNum(number)
e_n = GetRandNum(english_num,False)# not digits
print(n,e_n)
blankimg = Create_blank(width * number , height)
blankimg_en = Create_blank(width * english_num , height)
blankimg_all = Create_blank(width * (number + english_num),height)

cv2.imshow("all",blankimg)
img = CombineImage(blankimg,n,"digits")
img_en = CombineImage(blankimg_en,e_n,"english")

combine_img = CombineTwoImage(img,img_en)


ClearCombineImage(combine_img)
cv2.waitKey(0) 

	
	



