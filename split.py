import cv2
import numpy as np


img = cv2.imread('d.png')

print(img.shape)

w1_start = 35 
w1 = 130
h1_start = 0
h1 = 130
alph = ['a','b','c','d','e']

for index ,element in enumerate(alph):
    split_img = img[h1_start:h1,w1_start:w1+w1_start]
    cv2.imshow(alph[index],split_img)
    w1_start = w1_start + w1
    cv2.waitKey(0)
cv2.waitKey(0)