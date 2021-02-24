import cv2
import numpy as np

kernal = np.ones((5, 5), 'int8')

# CREATING IMAGE OBJECT
imgObj = cv2.imread('Resources/Photos/reonaldo.png')

# CONVERT COLOR SPACES
imgObjGray = cv2.cvtColor(imgObj, cv2.COLOR_BGR2GRAY)

# ADDING BLUR
imgObjBlur = cv2.GaussianBlur(imgObj, (11, 11), 0)

# CANNY IMAGE [IMAGE WITH BOUNDARY]
imgObjCanny = cv2.Canny(imgObj, 1000, 1000)

# IMAGE DIALATION [INCREASING THINKNESS OF IMAGE]
imgObjDia = cv2.dilate(imgObjCanny, kernel=kernal, iterations=1)

# IMAGE Erode [DECREASING THINKNESS OF IMAGE]
imgObjEro = cv2.erode(imgObjCanny, kernel=kernal, iterations=1)

# SHOW IMAGE OBJECT
cv2.imshow('Hello Image', imgObjDia)
cv2.waitKey(0)