import cv2
import math
import numpy as np
import os
import sys

centroid = (0, 0)
radius = 0
current = 0

def getNewEye(list):
    global currentEye
    if (current >= len(list)):
        if(current >= 2):
            current = 0
    newEye = list[currentEye]
    current +=1
    return (newEye)
    eyeList = []
def getIris(frame):
    iris=[]
if  __name__=='__main__':
    print __doc__
    try:
        fn=sys.argv[1]
    except:
        fn="../data/board.jpg"
    src=cv2.imread(fn,1)
    img=cv2.cvtColor(src,cv2.COLOR_RGB2GRAY)
    #print src.data
    img=cv2.medianBlur(img,5)
    #print img
    cimg=src.copy()
    circles=cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,10,np.array([]),100,30,1,30)
    #print img
    print circles
    a,b,c=circles.shape
    #print c
    #print circles.shape
    for i in range(b):
        cv2.circle(cimg,(circles[0][i][0],circles[0][i][1]),circles[0][i][2],(0,0,255),3,cv2.LINE_AA)
        cv2.circle(cimg,(circles[0][i][0],circles[0][i][1]),2,(0,255,0),3,cv2.LINE_AA)
    #cv2.imshow('source',src)
    cv2.imshow('detected',cimg)
    #cv2.dilate()
    cv2.waitKey(0)
    #img=cv2.imread("../data/lena.jpg",1)
    #print __doc__
    #cv2.imshow("ddd",img)
    #cv2.waitKey(0)
    