import cv2
import numpy as np

def Cut(width_start,width,height_start,height,interval,alph,img):
	for index ,element in enumerate(alph):
		split_img = img[height_start:height_start + height , width_start : width + width_start]
		cv2.imshow(alph[index],split_img)
		width_start = width_start + width + interval
		cv2.imwrite(alph[index]+".jpg", split_img)
		#cv2.waitKey(0)

img = cv2.imread('d.png')
img2 = cv2.imread('e.png')
cv2.imshow("all",img)
#cv2.imshow("all2",img2)

# the 1 layer
w1_start = 81
w1 = 56
h1_start = 13
h1 = 107
alph1 = ['a','b','c','d','e']

# the 2 layer
w2_start = 81
w2 = 56
h2_start = 209
h2 = 107
alph2 = ['f','g','h','i','j']

# the 3 layer
w3_start = 87
w3 = 57
h3_start = 384
h3 = 107
alph3 = ['k','l','m','n','o']

# the 4 layer
w4_start = 87
w4 = 57
h4_start = 582
h4 = 107
alph4 = ['p','q','r','s','t']

# the 5 layer

w5_start = 65
w5 = 65
h5_start = 42
h5 = 130
alph5 = ['u','v','w','x','y']

# the 6 layer

w6_start = 65
w6 = 65
h6_start = 237
h6 = 130
alph6 = ['z']

# the num1 layer

w7_start = 55
w7 = 65
h7_start = 405
h7 = 130
alph7 = ['1','2','3','4','5']

# the num2 layer

w8_start = 55
w8 = 65
h8_start = 620
h8 = 130
alph8 = ['6','7','8','9','0']


#Cut(w1_start,w1,h1_start,h1,70,alph1,img)
#Cut(w2_start,w2,h2_start,h2,70,alph2,img)
#Cut(w3_start,w3,h3_start,h3,71,alph3,img)
Cut(w4_start,w4,h4_start,h4,71,alph4,img)
#Cut(w5_start,w5,h5_start,h5,63,alph5,img2)
#Cut(w6_start,w6,h6_start,h6,63,alph6,img2)
#Cut(w7_start,w7,h7_start,h7,61,alph7,img2)
#Cut(w8_start,w8,h8_start,h8,61,alph8,img2)
cv2.waitKey(0)
