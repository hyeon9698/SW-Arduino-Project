import serial
import time

# 'COM3' 부분에 환경에 맞는 포트 입력
ser = serial.Serial('COM10', 9600)

while True:
    if ser.readable():
        val = ser.readline()
        if val.decode()[:len(val)-1] == 0:
            print(0)
        if val.decode()[:len(val)-1] == 1:
            print(1)
        if val.decode()[:len(val)-1] == 3:
            print(3)
        if val.decode()[:len(val)-1] == 4:
            print(4)
        if val.decode()[:len(val)-1] == 5:
            print(5)
        if val.decode()[:len(val)-1] == 6:
            print(6)
        print(val.decode()[:len(val)-1])  # 넘어온 데이터 중 마지막 개행문자 제외
