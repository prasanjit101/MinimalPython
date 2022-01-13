import cv2
import numpy as np


# for webcam argument should be 0 ,for mobile camera arg is 1
capture=cv2.VideoCapture(0)

while (1) :
    ret,frame=capture.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lower_green=np.array([80, 163, 105])
    upper_green=np.array([220, 255, 180])

    mask=cv2.inRange(hsv,lower_green,upper_green)
    kernel=np.ones((1,1),np.uint8)
    opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)

    finalImageMask=opening+closing
    res=cv2.bitwise_and(frame,frame,mask=finalImageMask)
    cv2.imshow('res',res)
    
    k = cv2.waitKey(5) & 0xFF # press esc to break 
    if k == 27:
        break

cv2.destroyAllWindows()
capture.release()   
