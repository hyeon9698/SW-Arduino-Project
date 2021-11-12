import serial
import numpy as np
import time
import cv2
from PIL import ImageFont, ImageDraw, Image # 한국어를 위한 import
# 'COM3' 부분에 환경에 맞는 포트 입력
ser = serial.Serial('COM10', 9600)
img0 = cv2.imread('0.jpg')
img1 = cv2.imread('1.jpg')
img2 = cv2.imread('2.jpg')
img3 = cv2.imread('3.jpg')
img4 = cv2.imread('4.jpg')
cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
font = cv2.FONT_HERSHEY_DUPLEX

cv2.imshow('window', img0)
cv2.waitKey()
while True:
    if ser.readable():
        val = ser.readline()
        if str(val.decode()[:len(val)-2]) == '0':
            print('작동 중지')
        if val.decode()[:len(val)-2] == '1':
            print('작동 시작')
        if val.decode()[:len(val)-2] == '3':
            img0 = img1
            cv2.imshow('window', img1)
        if val.decode()[:len(val)-2] == '4':
            img0 = img2
            cv2.imshow('window', img2)
        if val.decode()[:len(val)-2] == '5':
            img0 = img3
            cv2.imshow('window', img3)
        if val.decode()[:len(val)-2] == '6':
            img0 = img4
            cv2.imshow('window', img4)
        if val.decode()[:len(val)-2] == '7':
            tmp_img0 = img0
            val2 = ser.readline()
            image2 = Image.fromarray(img0)
            draw = ImageDraw.Draw(image2)
            draw.text((10, 20), "재고: " + str(val2.decode()[:len(val2)-2]), font=ImageFont.truetype("./batang.ttc", 48), fill=(0,0,255))
            img0 = np.array(image2)
            cv2.imshow('window', img0)
            img0 = tmp_img0
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # print(val.decode()[:len(val)-2])  # 넘어온 데이터 중 마지막 개행문자 제외
cv2.destroyAllWindows()