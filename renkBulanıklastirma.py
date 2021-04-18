import cv2
import numpy as np
kamera=cv2.VideoCapture("video.mp4")
while True:
    ret,frame=kamera.read()
    frame=cv2.resize(frame,(640,480))
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    blur=cv2.blur(hsv,(15,15))
    gaussianBlur=cv2.GaussianBlur(hsv,(15,15),0)
    median=cv2.medianBlur(hsv,15)
    
    cv2.imshow("blur",blur)
    cv2.imshow("gaussianBlur",gaussianBlur)
    cv2.imshow("median",median)


    if cv2.waitKey(25)& 0xFF==ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()


