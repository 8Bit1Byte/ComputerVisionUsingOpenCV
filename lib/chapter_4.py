import cv2
import numpy as np

# SHAPES AND TEXT ON IMGAES
def shape():
    imgNumPy = np.zeros((256, 256, 3), np.uint8)
    # imgNumPy[:] = 0, 0, 255

    # drawing line
    cv2.line(imgNumPy, (0,0), (256, 256), color= (0, 255, 0), thickness=2)
    cv2.rectangle(imgNumPy, (20, 10), (130, 100), color= (0, 0, 255), thickness= -1)
    cv2.circle(imgNumPy, (50, 50), radius= 20, color= (255, 0, 0))
    cv2.putText(imgNumPy, 'Hello Code', (50, 50), fontFace= cv2.FONT_ITALIC, fontScale= 1,color= (0, 255, 255), thickness= 1)

    cv2.imshow('Numpy Image', imgNumPy)
    cv2.waitKey(0)

if __name__ == '__main__':
    shape()
    