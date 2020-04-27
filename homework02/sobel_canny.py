# -*- coding: utf-8 -*-
import cv2
import time
import numpy as np
starttime = time.clock()
img = cv2.imread('people.jpg')#,cv2.IMREAD_GRAYSCALE)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)     #GRAY

#-------------------------------------------------------sobel
x = cv2.Sobel(img_gray,cv2.CV_16S,1,0)
y = cv2.Sobel(img_gray,cv2.CV_16S,0,1)
absX = cv2.convertScaleAbs(x)   
absY = cv2.convertScaleAbs(y)
sobel = cv2.addWeighted(absX,1,absY,1,0)

#-------------------------------------------------------gauss_sobel
result = cv2.GaussianBlur(img_gray,(5,5),0) 
result_x = cv2.Sobel(result,cv2.CV_16S,1,0)
result_y = cv2.Sobel(result,cv2.CV_16S,0,1)
result_absX = cv2.convertScaleAbs(result_x)   
result_absY = cv2.convertScaleAbs(result_y)
result_sobel = cv2.addWeighted(result_absX,1,result_absY,1,0)

#-------------------------------------------------------canny
canny = cv2.Canny(img_gray,10,250)

#contours, hierarchy = cv2.findContours(canny,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#for c in contours:
#    area = cv2.contourArea(c)
#    #print("area")
#    if area < 20 or area > 420000:
#        continue
#    #count+=1
#    (x, y, w, h) = cv2.boundingRect(c)
#    #((x1, y1), radius) = cv2.minEnclosingCircle(c)
#    g = h - w
#    #cv2.circle(img, (int(x1), int(y1)), int(radius), (0, 255, 0), 2)
#    if g >30 :
#        cv2.rectangle(img, (x, y), (x + w , y + h ), (0,0,255), 2)
#        rect = cv2.boundingRect(c) #提取矩形坐標



cv2.imshow('IMG',img)
cv2.imshow('sobel',sobel)
cv2.imshow('canny',canny)
cv2.imshow('result_sobel',result_sobel)
endtime = time.clock()
print ('time = ',endtime - starttime)




cv2.waitKey(0)
cv2.destroyAllWindows()
