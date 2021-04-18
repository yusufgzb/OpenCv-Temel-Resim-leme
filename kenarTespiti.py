import cv2
import numpy as np

orjinal=cv2.imread("lale.jpg")
gri=cv2.cvtColor(orjinal,cv2.COLOR_BGR2GRAY)

kenar=cv2.Canny(gri,125,255)

cv2.imshow("orjinal",orjinal)
cv2.imshow("kenar",kenar)

cv2.waitKey(0)
cv2.destroyAllWindows
