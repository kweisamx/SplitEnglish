import cv2
import numpy as np

def Cut(width_start,width,height_start,height,interval,alph,img):
	for index ,element in enumerate(alph):
		split_img = img[height_start:height_start + height , width_start : width + width_start]
		#cv2.imshow(alph[index],split_img)
		width_start = width_start + width + interval
		cv2.imwrite(alph[index]+".jpg", split_img)
		#cv2.waitKey(0)

img = cv2.imread('d.png')
img2 = cv2.imread('e.png')
cv2.imshow("all",img)
cv2.imshow("all2",img2)

# the 1 layer
w1_start = 75
w1 = 65
h1_start = 0
h1 = 130
alph1 = ['a','b','c','d','e']

# the 2 layer
w2_start = 75
w2 = 65
h2_start = 190
h2 = 130
alph2 = ['f','g','h','i','j']

# the 3 layer
w3_start = 85
w3 = 65
h3_start = 380
h3 = 130
alph3 = ['k','l','m','n','o']

# the 4 layer
w4_start = 85
w4 = 65
h4_start = 570
h4 = 130
alph4 = ['p','q','r','s','t']

# the 5 layer

w5_start = 65
w5 = 65
h5_start = 35
h5 = 130
alph5 = ['u','v','w','x','y']

# the 6 layer

w6_start = 65
w6 = 65
h6_start = 230
h6 = 130
alph6 = ['z']

# the num1 layer

w7_start = 55
w7 = 65
h7_start = 410
h7 = 130
alph7 = ['1','2','3','4','5']

# the num2 layer

w8_start = 55
w8 = 65
h8_start = 620
h8 = 130
alph8 = ['6','7','8','9','0']


Cut(w1_start,w1,h1_start,h1,62,alph1,img)
Cut(w2_start,w2,h2_start,h2,62,alph2,img)
Cut(w3_start,w3,h3_start,h3,62,alph3,img)
Cut(w4_start,w4,h4_start,h4,62,alph4,img)
Cut(w5_start,w5,h5_start,h5,63,alph5,img2)
Cut(w6_start,w6,h6_start,h6,63,alph6,img2)
Cut(w7_start,w7,h7_start,h7,61,alph7,img2)
Cut(w8_start,w8,h8_start,h8,61,alph8,img2)
cv2.waitKey(0)
