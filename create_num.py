import cv2
import numpy as np
from random import randint

#CONST
height = 107
width = 57
number = 4
english_num= 3
english_map = dict(zip((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25),('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')))
resize_zoom = 1.65

def Create_blank(width, height, rgb_color=(255, 255, 255)):
    """Create new image(numpy array) filled with certain color in RGB"""
    # Create black blank image
    image = np.zeros((height, width, 3), np.uint8)

    # Since OpenCV uses BGR, convert the color first
    color = tuple(reversed(rgb_color))
    # Fill image with color
    image[:] = color

    return image

def GetRandNum(number,digist=True):
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
    w1_start = 0
    for i in range(len(element)):
        element_img = cv2.imread(element[i]+'.jpg')
        h1,w1,_ = element_img.shape
        blank[:h1 , w1_start : w1_start + w1 ,:3] = element_img
        w1_start = w1_start +w1
        if i != len(element) - 1 :
            blank[:h1 , w1_start:w1_start + 4,:3] = Create_blank(4,h1)
            w1_start = w1_start + 4
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
    ret,binary = cv2.threshold(gray,230,255,cv2.THRESH_BINARY) # change the image to black and write
    #binary = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
 #   _ , contours, hierarchy  =  cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
 #   print(len(contours))
 #   cv2.drawContours(img,contours,-1,(0,0,0),1)  
    cv2.imshow("img", binary)  
    cv2.waitKey(0) 


def resize(img, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h,w) = img.shape[:2]
    if width == None:
        r = height/float(h)
        dim = (int(w * r), height)
    else:
        r= width / float(w)
        dim = (width, int(h * r))
    resized = cv2.resize(img, dim, interpolation=inter)
    return resized



n = GetRandNum(number)
e_n = GetRandNum(english_num,False)# not digits
print(n,e_n)
blankimg = Create_blank(width * number + (number-1) * 4 , height)
blankimg_en = Create_blank(width * english_num + (english_num-1) * 4 , height)
blankimg_all = Create_blank(width * (number + english_num) +(number+ english_num - 2) * 4 ,height)

cv2.imshow("all",blankimg)
img = CombineImage(blankimg,n,"digits")
img_en = CombineImage(blankimg_en,e_n,"english")

combine_img = CombineTwoImage(img,img_en)
(h,w) = combine_img.shape[:2]

#resize_img = resize(combine_img,width = combine_img.shape[1] * 2, inter=cv2.INTER_AREA)
resize_img = cv2.resize(combine_img, (int(w * resize_zoom) ,int( h * resize_zoom) ), interpolation=cv2.INTER_CUBIC)
cv2.imshow("resize",resize_img)

#ClearCombineImage(combine_img)
cv2.waitKey(0) 

	
	



