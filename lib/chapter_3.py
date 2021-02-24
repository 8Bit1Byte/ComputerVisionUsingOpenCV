import cv2
import numpy as np

def reshape():
    imgObj = cv2.imread('Resources/Photos/reonaldo.png')
    print(imgObj.shape)

    reshaped = cv2.resize(imgObj, (int(imgObj.shape[0]/2), int(imgObj.shape[1]/2)))

    cv2.imshow('Resized Image', reshaped)
    cv2.waitKey(0)

def crop():
    imgObj = cv2.imread('Resources/Photos/Small.jpg')
    print(imgObj.shape)
    print(imgObj)

    croped = imgObj[0,0:2]
    print('--\n', croped)

    cv2.imshow('Croped Image', croped)
    cv2.waitKey(0)

crop()
# if __name__ =='__main__':
#     print('Program Started')
#     num = input('ENTER GIVEN NUMBER : \n   [1] => ImageShow Call \n   [2] => VideoShow Call \n   [3] => WebCamShow Call \n TICK : ')
#     switcher = {
#         '1':reshape,
#         '2':crop,
#     }
#     switcher[num]()
#     print('Program End')