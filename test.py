import numpy as np
import cv2

contours = np.array( [ [50,50], [50,150], [150, 150], [150,50] ] )
img = np.zeros( (200,200) ) # create a single channel 200x200 pixel black image 
cv2.fillPoly(img, pts =[contours], color=(255,255,255))
cv2.imshow(" ", img)
cv2.waitKey()
