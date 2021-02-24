from types import CoroutineType
import cv2
import numpy as np


kernal = np.ones((5, 5), 'int8')
# Working with <Image, Video, WebCam>
def imageShow():
    imgObj = cv2.imread('Resources\\Photos\\lamborghini.jpg')
    cv2.imshow('Image Show', imgObj)
    while not (cv2.waitKey(1) == ord('q')):
        if cv2.waitKey(1) == ord('q'):
            print('Key Pressed')    
            cv2.destroyAllWindows()
            return 0

def videoShow():
    vidObj =  []
    for i in range(1, 10):
        vidObj.append(cv2.imread(f'Resources\\Photos\\ColorSet\\{i}.png'))
    
    for i in range(len(vidObj)):
        cv2.imshow('Video Show', vidObj[i])
        cv2.waitKey(100)

def webCamShow():
    vidObj = cv2.VideoCapture(0)
    vidObj.set(3, 60)
    vidObj.set(4, 60)
    vidObj.set(10, 100)
    success = True

    while success:
        success, imgObj = vidObj.read()
        if (not success) or (cv2.waitKey(1) == ord('q')):
            break
        
        cv2.imshow('Web Cam Show',imgObj)
        cv2.waitKey(1)

# Working with basic Function
def basic():
    imgObj = cv2.imread('Resources\\Photos\\lamborghini.jpg')

    # convertColor
    imgGray = cv2.cvtColor(imgObj, cv2.COLOR_BGR2GRAY)

    # blur Effect
    imgBlur = cv2.GaussianBlur(src=imgObj, ksize= (11, 11), sigmaX= 0)

    # canny Effect
    imgCanny = cv2.Canny(imgObj, threshold1= 200, threshold2= 100)

    # dialation Effect
    imgDia = cv2.dilate(imgCanny, kernel= kernal, iterations= 1)

    # erode Effect
    imgErode = cv2.erode(imgDia, kernel= kernal, iterations= 1)

    cv2.imshow('Image Show', imgErode)
    cv2.waitKey(0)

# Working with Resizing and Cropping
def resizing():
    imgObj = cv2.imread('Resources\\Photos\\lamborghini.jpg')
    resizedObj = cv2.resize(imgObj, tuple(map(int, (imgObj.shape[1]/2, imgObj.shape[0]/2))))

    cv2.imshow('Resized Image', resizedObj)
    cv2.waitKey(0)

def crop():
    imgObj = cv2.imread('Resources\\Photos\\lamborghini.jpg')
    cropObj = imgObj[::,::,2]

    cv2.imshow('Resized Image', cropObj)
    cv2.waitKey(0)


if __name__ == '__main__':
    print('Program Started')
    num = input('ENTER GIVEN NUMBER : \n   '+
                '[1] => ImageShow Call \n   '+
                '[2] => VideoShow Call \n   '+
                '[3] => WebCamShow Call \n  '+
                ' [4] => Basic Function \n   '+
                '[5] => Resizing Image \n   '+
                '[6] => Crop Image \n TICK : ')
    print('\n+-------------------------------+\n')
    switcher = {
        '1':imageShow,
        '2':videoShow,
        '3':webCamShow,
        '4':basic,
        '5':resizing,
        '6':crop
    }
    result = switcher[num]
    result()
    print('Program End')