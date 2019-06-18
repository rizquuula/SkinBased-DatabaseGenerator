import cv2
import numpy as np 
import time 

cam = cv2.VideoCapture(0)
cam.set(3,300)
cam.set(4,300)
cam.set(cv2.CAP_PROP_FPS, 3)
img_size = 100
boolean = 1
num = -10
last_time = time.time()

while boolean:
    ret, frame = cam.read()
    min_color = np.array([0, 10, 10], dtype = "uint8")
    max_color = np.array([35, 255, 255], dtype = "uint8")
    HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(HSV, min_color, max_color)
    #skinHSV = cv2.bitwise_and(frame, frame, mask = skinRegionHSV)
    #skinHSV = cv2.cvtColor(frame, cv2.BGR2GRAY)
    #cv2.imshow('Capturing start', frame)
    blur = cv2.medianBlur(mask, 5)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10,10))
    res = cv2.dilate(blur, kernel)

    filterImg = cv2.erode(mask,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))) #eroding the image
	#cv2.imshow("img5",filterImg)
    
    filterImg = cv2.dilate(filterImg,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))) #dilating the image
    #cv2.imshow("img6",filterImg)

    cv2.namedWindow("img 0")
    cv2.imshow('img 0', frame)
    cv2.namedWindow("img 1")
    cv2.imshow('img 1', HSV)
    cv2.namedWindow("img 2")
    cv2.imshow('img 2', mask)
    cv2.namedWindow("img 3")
    cv2.imshow('img 3', res)
    #cv2.namedWindow("img 4")
    #cv2.imshow('img 4', filterImg)
    #cv2.imshow('Capturing start', np.hstack([frame, skinRegionHSV]))
    #time.sleep(500)
    #now = time.time() - last_time
    #minute = now / 60
    #seconds = now % 60
    #print ('Timer '+str(int(minute))+'minute(s) :'+str(int(seconds))+' second(s)')
    num+=1
    print (num)
    if num>=0:
        name = str('Six'+str(num)+'.jpg')
        cv2.imwrite(name,res)
        name2 = str('SixMask'+str(num)+'.jpg')
        cv2.imwrite(name2,mask)
    elif (num == 1000):
        boolean=0
    '''for i in range(1000):
        name = str(str(i)+'.jpg')
        cv2.imwrite(name,res)
        if (i == 999):
            boolean = 0'''
    if cv2.waitKey(1) & 0xFF == ord('q'):
        boolean = 0

cam.release()
cv2.destroyAllWindows()