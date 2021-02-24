import cv2

# FOR IMAGES
def imageShow():
    imgObj = cv2.imread('Resources\\Photos\\messi.jpg')

    cv2.imshow('Hello Image', imgObj)
    if cv2.waitKey(0) == ord('q'):
        cv2.destroyAllWindows()

# FOR VIDEOS
def videoShow():
    vidObj = cv2.VideoCapture('Resources\\Videos\\dog.mp4')
    success = True

    while success:
        success, imgObj = vidObj.read()
        if (not success) or (cv2.waitKey(1) == ord('q')):
            break

        cv2.imshow('Hello Video', imgObj)
        cv2.waitKey(1)

# FOR WEBCAMS
def webCamShow():
    webObj = cv2.VideoCapture(0)

    webObj.set(3, 1920)
    webObj.set(4, 1080)

    success = True
    while success:
        success, obj = webObj.read()
        if (not success) or (cv2.waitKey(1) == ord('q')):
            break

        cv2.imshow('Hello WebCam', obj)
        cv2.waitKey(1)

if __name__ == '__main__':
    print('Program Started')
    num = input('ENTER GIVEN NUMBER : \n   [1] => ImageShow Call \n   [2] => VideoShow Call \n   [3] => WebCamShow Call \n TICK : ')
    switcher = {
        '1':imageShow,
        '2':videoShow,
        '3':webCamShow
    }
    switcher[num]()
    print('Program End')
    


