from create_num import *
import sys
from optparse import OptionParser
from erode_dilate import *

# Set parse

parser = OptionParser()  
parser.add_option("-c","--create", action="store_true",dest="create",help="save the image to current directory") 
parser.add_option("-e","--erode", action="store_true",dest="erode",help="erode the img") 
parser.add_option("-d","--dilate", action="store_true",dest="dilate",help="dilate") 
parser.add_option("-s","--struct-size",type="int",dest="struct_element",help="input the structuring element size",default=1)
parser.add_option("-n","--name",dest="name",help="input the name which you want to creaete",default=None)
parser.add_option("-z","--zoom-size",type="float",dest="zoom_size",help="input the zoom size you want resize",default=resize_zoom)
(options, args) = parser.parse_args()




# The input of License Plate Number

LPN_input = options.name

resize_zoom = options.zoom_size

se = options.struct_element

# If no input, the number will be randomly created

if LPN_input!=None:
    SplitLPN = list(LPN_input)
    print(SplitLPN)
    number = len(SplitLPN)
    # Create the blankimg of the LPN_input
    LPN_blankimg = Create_blank(width * number + (number - 1) * interval , height)
    
    combine_img = CombineImage(LPN_blankimg,LPN_input,"manaual")
else:
    n = GetRandNum(number)
    e_n = GetRandNum(english_num,False)# not digits
    print(n,e_n)
    blankimg = Create_blank(width * number + (number-1) * interval , height)
    blankimg_en = Create_blank(width * english_num + (english_num-1) * interval , height)
    #blankimg_all = Create_blank(width * (number + english_num) +(number+ english_num - 2) * 4 ,height)

    cv2.imshow("all",blankimg)
    img = CombineImage(blankimg,n,"digits")
    img_en = CombineImage(blankimg_en,e_n,"english")

    combine_img = CombineTwoImage(img,img_en)

(h,w) = combine_img.shape[:2]

print(w,w * resize_zoom ,h, h*resize_zoom)

if options.erode:
    combine_img = Erode(combine_img,se)
if options.dilate:
    combine_img = Dilate(combine_img,se)

# Resize the img size
resize_img = cv2.resize(combine_img, (int(w * resize_zoom) ,int( h * resize_zoom) ), interpolation=cv2.INTER_AREA)
cv2.imshow("resize",resize_img)

if options.create:
    cv2.imwrite(LPN_input+'_fake.jpg',resize_img)
cv2.waitKey(0) 

	
	



