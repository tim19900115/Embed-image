import os
import cv2
from math import *
import numpy as np
import matplotlib.pyplot as plt
import datetime
import time
import threading


starttime = datetime.datetime.now()
    


path = "D:/test/"           #設定路徑
filenames = os.listdir(path) 
#print(filenames)
#dilation_canny_img = np.zeros
for file in filenames:         
    #def __init__(self):
    img = cv2.imread(path+file)
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  

    kernel = np.ones((3,3),np.uint8)      
    h, w = img.shape[:2]
    mask = np.zeros([h+2, w+2], np.uint8)
    mask_2 = np.zeros([h, w], np.uint8)
    #all_bub = 0
    def thresh():
        ret, img_threshold = cv2.threshold(img_gray,150,255,cv2.THRESH_BINARY_INV)                           #img二值化
        ret, img_threshold_inv = cv2.threshold(img_gray,150,255,cv2.THRESH_BINARY)                           #img二值化    
        cv2.floodFill(img_threshold_inv, mask, (100, 80), (0, 50, 255), (100, 100, 50), (50, 50, 50), cv2.FLOODFILL_FIXED_RANGE)
        img_threshold_new = cv2.bitwise_or(img_threshold,img_threshold_inv)


        dimg=cv2.pyrDown(img_threshold_new)
        dimg1=cv2.pyrDown(dimg)
        uimg1=cv2.pyrUp(dimg1)
        uimg2=cv2.pyrUp(uimg1)    
        
####################################################################################################################################################

        add_uimg = cv2.addWeighted(img_threshold_new,0.3,uimg2,0.7,0) 
        add_uimg1 = cv2.addWeighted(add_uimg,0.4,uimg2,0.6,0) 
        add_uimg2 = cv2.addWeighted(add_uimg1,0.4,uimg2,0.6,0) 
        add_uimg3 = cv2.addWeighted(add_uimg2,0.4,uimg2,0.6,0)
        
        canny_img = cv2.Canny(add_uimg, 40, 150)
        canny_img1 = cv2.Canny(add_uimg1, 40, 150)
        canny_img2 = cv2.Canny(add_uimg2, 40, 150)
        canny_img3 = cv2.Canny(add_uimg3, 40, 150)
        
        #global dilation_canny_img
        dilation_canny_img = cv2.dilate(canny_img1,kernel,iterations=1)           
        img_new_99 = np.copy(dilation_canny_img)
        #return dilation_canny_img

####################################################################################################################################################
    #def hough():
        #global dilation_canny_img
        c = cv2.HoughCircles(dilation_canny_img, cv2.HOUGH_GRADIENT, 1, 20, param1=15, param2=25, minRadius=4, maxRadius=35)    
        c = np.uint16(np.around(c))
        for i in c[0,:]:
            cv2.circle(mask_2, (i[0], i[1]), i[2], (255, 255, 255), -1)
            cv2.circle(img_new_99, (i[0], i[1]), i[2], (0, 0, 0), 8) 
        
####################################################################################################################################################
        c = cv2.HoughCircles(img_new_99, cv2.HOUGH_GRADIENT, 1, 30, param1=25, param2=18, minRadius=4, maxRadius=50)     
        c = np.uint16(np.around(c))
        for i in c[0,:]:
            cv2.circle(mask_2, (i[0], i[1]), i[2]+5, (255, 255, 255), -1)
####################################################################################################################################################
    #def count():
        c = cv2.HoughCircles(mask_2, cv2.HOUGH_GRADIENT, 1, 20, param1=15, param2=12, minRadius=2, maxRadius=55)     #####總
        c = np.uint16(np.around(c))
        global f
        f = []
        
        for i in c[0,:]:
            cv2.circle(img, (i[0], i[1]), i[2], (0, 0, 255), 3)
            f.append(i[2])
        global all_bub
        all_bub = len(f)
        #u = all_bub
        #time.sleep(1)
        #return all_bub



####################################################################################################################################################

    def main():
        t1 = threading.Thread(target=thresh)
        #t2 = threading.Thread(target=hough)
        t1.start()
        #t2.start()
        time.sleep(1)
        #print(all_bub) 


    if __name__ == '__main__':
        main()
    #thresh()
        
    #print(u) 
        #threading.Thread(target=hough).start()
        #threading.Thread(target=count).start()  
    #thread()
   
    
    plt.hist(f, bins =  [c for c in range (1,45)])
    cv2.putText(img, str(all_bub), (10, 60), cv2.FONT_HERSHEY_SIMPLEX,2, (255, 255, 255), 6)
    cv2.putText(img, str(all_bub), (10, 60), cv2.FONT_HERSHEY_SIMPLEX,2, (0, 0, 0), 3)


    #cv2.imwrite('.\B_output_data\image (%d).jpg'%(a), img_1)
    #cv2.imwrite('image (197).jpg', img)

    cv2.imshow('IMG',cv2.pyrDown(img))
    #cv2.imshow('IMG',cv2.pyrDown(dilation_canny_img))
    

    
    #plt.savefig('.\B_output_data\image (%d).png'%(a))
    plt.title("bubble_radius")     
    plt.show()
    #plt.pause(1)
    #plt.cla()   # Clear axis
    #plt.clf()   # Clear figure
    #plt.close()
    #cv2.imshow('IMG7',cv2.pyrDown(img_new_2))
    ##cv2.imshow('IMG8',cv2.pyrDown(sobel_bitwiseXor_dilation))
    #cv2.imshow('IMG',cv2.pyrDown(uimg1))
    cv2.waitKey(0)

    #cv2.waitKey(0)
endtime = datetime.datetime.now()
print ((endtime - starttime).seconds)





cv2.destroyAllWindows()

