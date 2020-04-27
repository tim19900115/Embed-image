# -*- coding: utf-8 -*-
import cv2
import time
import numpy as np

img = cv2.imread('hero.jpg')#,cv2.IMREAD_GRAYSCALE)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, img_threshold = cv2.threshold(img_gray,128,255,cv2.THRESH_BINARY)
cv2.imshow('IMG',img)

cv2.setUseOptimized(False) # AVX
#cv2.setUseOptimized(True) # AVX
print(cv2.useOptimized())
kernel_3 = np.ones((3,3),np.uint8)
kernel_5 = np.ones((5,5),np.uint8)
kernel_7 = np.ones((7,7),np.uint8)
kernel_9 = np.ones((9,9),np.uint8)

starttime_3_open = time.clock()
opening_3 = cv2.morphologyEx(img_threshold,cv2.MORPH_OPEN,kernel_3,1000)
cv2.imshow('Open_3',opening_3)
endtime_3_open = time.clock()
print ('3 X 3_open = ',endtime_3_open - starttime_3_open)

starttime_3_close = time.clock()
closing_3 = cv2.morphologyEx(img_threshold,cv2.MORPH_CLOSE,kernel_3,1000)
cv2.imshow('Close_3',closing_3)
endtime_3_close = time.clock()
print ('3 X 3_close = ',endtime_3_close - starttime_3_close)

starttime_5_open = time.clock()
opening_5 = cv2.morphologyEx(img_threshold,cv2.MORPH_OPEN,kernel_5,1000)
cv2.imshow('Open_5',opening_5)
endtime_5_open = time.clock()
print ('5 X 5_open = ',endtime_5_open - starttime_5_open)

starttime_5_close = time.clock()
closing_5 = cv2.morphologyEx(img_threshold,cv2.MORPH_CLOSE,kernel_5,1000)
cv2.imshow('Close_5',closing_5)
endtime_5_close = time.clock()
print ('5 X 5_close = ',endtime_5_close - starttime_5_close)

starttime_7_open = time.clock()
opening_7 = cv2.morphologyEx(img_threshold,cv2.MORPH_OPEN,kernel_7,1000)
cv2.imshow('Open_7',opening_7)
endtime_7_open = time.clock()
print ('7 X 7_open = ',endtime_7_open - starttime_7_open)

starttime_7_close = time.clock()
closing_7 = cv2.morphologyEx(img_threshold,cv2.MORPH_CLOSE,kernel_7,1000)
cv2.imshow('Close_7',closing_7)
endtime_7_close = time.clock()
print ('7 X 7_close= ',endtime_7_close - starttime_7_close)

starttime_9_open = time.clock()
opening_9 = cv2.morphologyEx(img_threshold,cv2.MORPH_OPEN,kernel_9,1000)
cv2.imshow('Open_9',opening_9)
endtime_9_open = time.clock()
print ('9 X 9_open = ',endtime_9_open - starttime_9_open)

starttime_9_close = time.clock()
closing_9 = cv2.morphologyEx(img_threshold,cv2.MORPH_CLOSE,kernel_9,1000)
cv2.imshow('Close_9',closing_9)
endtime_9_close = time.clock()
print ('9 X 9_close = ',endtime_9_close - starttime_9_close)


cv2.waitKey(0)
cv2.destroyAllWindows()
