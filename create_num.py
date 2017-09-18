import cv2
import numpy as np
from random import randint
def create_blank(width, height, rgb_color=(0, 0, 0)):
	"""Create new image(numpy array) filled with certain color in RGB"""
	# Create black blank image
	image = np.zeros((height, width, 3), np.uint8)

	# Since OpenCV uses BGR, convert the color first
	color = tuple(reversed(rgb_color))
	# Fill image with color
	image[:] = color

	return image

height = 130
width = 35

number = 3

randnum = []
for i in range(number):
	randnum.append(str(randint(0,9)))
print(randnum)

blankimg = 



	
	



