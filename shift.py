import cv2
import numpy as np
from optparse import OptionParser


parser = OptionParser()
parser.add_option("-f","--filename",metavar="FILE",help="the input data",dest="filename")
(options,args) = parser.parse_args()


img_path = options.filename

# load image
img = cv2.imread(img_path)

# shift the image
M = np.float32([[1,0,45],[0,1,10]])
shifted = cv2.warpAffine(img.copy(),M,(180,40))

cv2.imwrite("a.jpg",shifted)
cv2.imshow("shift",shifted)
cv2.waitKey(0)
