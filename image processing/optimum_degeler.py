import cv2 as c
import numpy as np
from datetime import datetime


camera = c.VideoCapture(0)

while True:
    
    ret, img=camera.read()
    
    
    hsv = c.cvtColor(img, c.COLOR_BGR2HSV)
    
    myMask=c.inRange(hsv, (0,100,20), (10,255,255)) #optimum değerler
    masked_img=c.bitwise_and(img, img, mask=myMask)
    
    
    #c.imshow("masked window", masked_img)
    
    
    c.imshow("real img", img)
    
    
    
    if c.waitKey(20) & 0xFF == ord("q"):
        break
    if c.waitKey(20) & 0xFF == ord("s"):
        
        now = datetime.now()
        
        c.imwrite("saved_img.png", img)
    

camera.release()
c.destroyAllWindows()

