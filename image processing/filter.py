import cv2 as c
import numpy as np

camera = c.VideoCapture(0)

while 1:
    ret, image=camera.read()
    
    len_max=np.array([135,255,255])
    len_min=np.array([30,30,30])
    
    mask=c.inRange(image, len_min, len_max)
    lastImage = c.bitwise_and(image, image, mask=mask)
    
    c.imshow("our mask window", mask)
    c.imshow("masked window", lastImage)
    c.imshow("normal window", image)
    
    if c.waitKey(25) & 0xFF==ord("q"):
        break

camera.release()
c.destroyAllWindows()

    