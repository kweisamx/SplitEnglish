import cv2
import numpy as np


def GetStructuringElement(struct_num):
    # Create Structuring Element
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
    return kernel


# Erode the image
def Erode(img,struct_num):

    kernel = GetStructuringElement(struct_num)
    eroded = cv2.erode(img,kernel)
    #cv2.imshow('Erode Image',eroded)
    return eroded

# dilate the image
def Dilate(img,struct_num):
    kernel = GetStructuringElement(struct_num)
    dilated = cv2.dilate(img, kernel)
    #cv2.imshow('Dilated Imagea', dilated)
    return dilated



