from create_num import *
import sys
from optparse import OptionParser


# Set parse

parser = OptionParser()
parser.add_option("-f","--fake",type='bool',dest='fake')


# The input of License Plate Number

LPN_input = None if len(sys.argv) <= 1 else sys.argv[1] 



# If no input, the number will be randomly created

if LPN_input!=None:
    SplitLPN = list(LPN_input)
    print(SplitLPN)
    number = len(SplitLPN)
    # Create the blankimg of the LPN_input
    LPN_blankimg = Create_blank(width * number + (number - 1) * 4 , height)
    combine_img = CombineImage(LPN_blankimg,LPN_input,"manaual")
    cv2.imwrite(LPN_input+'_fake.jpg',combine_img)
    cv2.waitKey(0)
    
else:
    n = GetRandNum(number)
    e_n = GetRandNum(english_num,False)# not digits
    print(n,e_n)
    blankimg = Create_blank(width * number + (number-1) * 4 , height)
    blankimg_en = Create_blank(width * english_num + (english_num-1) * 4 , height)
    #blankimg_all = Create_blank(width * (number + english_num) +(number+ english_num - 2) * 4 ,height)

    cv2.imshow("all",blankimg)
    img = CombineImage(blankimg,n,"digits")
    img_en = CombineImage(blankimg_en,e_n,"english")

    combine_img = CombineTwoImage(img,img_en)
    (h,w) = combine_img.shape[:2]

    #resize_img = resize(combine_img,width = combine_img.shape[1] * 2, inter=cv2.INTER_AREA)
    print(w,w * resize_zoom ,h, h*resize_zoom)
    resize_img = cv2.resize(combine_img, (int(w * resize_zoom) ,int( h * resize_zoom) ), interpolation=cv2.INTER_AREA)
    cv2.imshow("resize",resize_img)
    cv2.imwrite("test.jpg",resize_img)
    #AffineImage(resize_img,"affine")
    #PerspectiveImage(resize_img,"P_img")
    #ClearCombineImage(combine_img)
    cv2.waitKey(0) 

	
	



