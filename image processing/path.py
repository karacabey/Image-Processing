import cv2 as c
import numpy as np

img=c.imread("myimg.jpeg")





while True:
    img_gray = c.cvtColor(img, c.COLOR_BGR2GRAY)
    
    th, img_thres=c.threshold(img_gray, 200, 255, c.THRESH_BINARY)
    kernel=np.ones((15,15),np.float32)/255
    smoothed = c.filter2D(img_thres , -1, kernel)
    
    c.imshow("path", img_gray)
    c.imshow("thresh", img_thres)
    c.imshow("smoothed", smoothed)
    
    if c.waitKey(20) & 0xFF==ord("q"):
        break

c.destroyAllWindows()
