import cv2
import numpy as np

img = cv2.imread('/Users/advaybajaj/Desktop/plants4.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (21,21), 0)

_,thr = cv2.threshold(blur, 120, 255, cv2.THRESH_BINARY_INV)

cont,_ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for i in cont:
    area = cv2.contourArea(i)
    if area > 1000:
        cv2.drawContours(img, [i], -1, (0,20,240), 2)

cv2.imshow('img', img)

cv2.waitKey(0)    
cv2.destroyAllWindows()
#cam.release()