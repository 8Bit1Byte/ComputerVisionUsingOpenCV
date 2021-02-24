import numpy as np
import cv2

# WRAP PERSPECTIVE
def wrapPers():
    imgObj = cv2.imread('Resources\\Photos\\cards.png')
    widht = 250
    height = 350

    # decalaring prespective for given edge and corener
    edges = np.float32([[305, 75], [385, 150], [230, 230], [150, 160]])
    corner = np.float32([[0, 0], [widht, 0], [widht, height], [0, height]])
    
    materx = cv2.getPerspectiveTransform(edges, corner)
    outImg = cv2.warpPerspective(imgObj, materx, (widht, height))

    cv2.imshow('Input Show', imgObj)
    cv2.imshow('Output Show', outImg)
    cv2.waitKey(0)


if __name__ == '__main__':
    wrapPers()