import serial
import numpy as np
import time
import cv2
from PIL import ImageFont, ImageDraw, Image # 한국어를 위한 import
import cvlib as cv
from cvzone.SerialModule import SerialObject
from datetime import datetime, timedelta
from pytz import timezone
import telegram
from dotenv import load_dotenv
import os
import matplotlib.pyplot as plt
import pandas as pd
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters

load_dotenv()
master_token = os.getenv('TELEGRAM_API_TOKEN_KEY')
master_mc = os.getenv('TELEGRAM_API_MC')
master_bot = telegram.Bot(master_token)

now = datetime.now(timezone('Asia/Seoul'))
msg = f"{now.strftime('%Y-%m-%d %H:%M:%S')} 프로그램이 시작되었습니다. 부팅 20초 정도 소요됩니다.\n"
master_bot.sendMessage(master_mc,msg)
# 'COM3' 부분에 환경에 맞는 포트 입력
ser = serial.Serial('COM7', 9600)
img0 = cv2.imread('0.jpg')
img1 = cv2.imread('1.jpg')
img2 = cv2.imread('2.jpg')
img3 = cv2.imread('3.jpg')
img4 = cv2.imread('4.jpg')
black = cv2.imread('black.jpg')
cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
font = cv2.FONT_HERSHEY_DUPLEX
arduino = SerialObject('COM6')

age_net = cv2.dnn.readNetFromCaffe(
    'models/deploy_age.prototxt', 
    'models/age_net.caffemodel')
age_list_final = ['(0, 6)','(8, 20)','(23, 100)']
cv2.imshow('window', img0)
onoff = 1
ondisplay = 1
# updater
updater = Updater(token=master_token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()
x = input('준비가 완료 되었습니다. 엔터를 눌러주세요')
cv2.waitKey()
while True:
    if ser.readable():
        val = ser.readline()
        print(val.decode()[:len(val)-2])
        if val.decode()[:len(val)-2] == '8':
            # CAM
            # 객체 생성
            msg = f"카메라가 실행됩니다."
            master_bot.sendMessage(master_mc,msg)
            cap = cv2.VideoCapture(1)
            stop_signal = 0
            def handler(update, context):
                global stop_signal
                user_text = update.message.text # 사용자가 보낸 메세지를 user_text 변수에 저장합니다.
                if user_text == "stop":
                    stop_signal = 1
                    master_bot.send_message(chat_id=master_mc, text="stopping camera") # 답장 보내기
                if user_text == "help":
                    master_bot.send_message(chat_id=master_mc, text="stop 을 입력하면 카메라 종료\nstop 를 입력하면 sensor 종료 ") # 답장 보내기
            
            echo_handler = MessageHandler(Filters.text, handler)
            dispatcher.add_handler(echo_handler)
            # cap = cv2.VideoCapture(1)
            # arduino = SerialObject('COM6')

            # age_net = cv2.dnn.readNetFromCaffe(
            #     'models/deploy_age.prototxt', 
            #     'models/age_net.caffemodel')
            # age_list_final = ['(0, 6)','(8, 20)','(25, 100)']
            cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
            img0 = cv2.imread('0.jpg')
            img1 = cv2.imread('1.jpg')
            img2 = cv2.imread('2.jpg')
            img3 = cv2.imread('3.jpg')
            img4 = cv2.imread('4.jpg')
            img11 = cv2.imread('11.jpg')
            img12 = cv2.imread('12.jpg')
            img13 = cv2.imread('13.jpg')
            img14 = cv2.imread('14.jpg')
            img15 = cv2.imread('15.jpg')
            img16 = cv2.imread('16.jpg')
            img17 = cv2.imread('17.jpg')
            img18 = cv2.imread('18.jpg')
            img19 = cv2.imread('19.jpg')
            img20 = cv2.imread('20.jpg')
            img21 = cv2.imread('21.jpg')
            img22 = cv2.imread('22.jpg')
            img23 = cv2.imread('23.jpg')
            img24 = cv2.imread('24.jpg')
            img25 = cv2.imread('25.jpg')
            img26 = cv2.imread('26.jpg')
            img27 = cv2.imread('27.jpg')
            img28 = cv2.imread('28.jpg')
            img29 = cv2.imread('29.jpg')
            img30 = cv2.imread('30.jpg')
            img31 = cv2.imread('31.jpg')
            img32 = cv2.imread('32.jpg')
            img33 = cv2.imread('33.jpg')
            img34 = cv2.imread('34.jpg')
            img35 = cv2.imread('35.jpg')
            img36 = cv2.imread('36.jpg')
            img37 = cv2.imread('37.jpg')
            img38 = cv2.imread('38.jpg')
            img39 = cv2.imread('39.jpg')
            img40 = cv2.imread('40.jpg')
            img41 = cv2.imread('41.jpg')
            img42 = cv2.imread('42.jpg')

            cv2.imshow('window', img0)
            label = 'male'
            TIME = 0 # 0 이면 낮 1이면 밤
            skip_index = 0
            no_face_count = 0
            while True:
                if stop_signal == 1:
                    break
                now = datetime.now(timezone('Asia/Seoul'))
                if 0 < now.hour < 10 and 22 < now.hour < 24:
                    TIME = 1
                    # print('밤')
                else:
                    TIME = 0
                    # print('낮')
                success, im = cap.read()
                if not success:
                    print('no frame')
                    continue
                faces, confidences = cv.detect_face(im)
                both_gender = {'male': 0, 'female': 0}
                face_max_index = 0
                # print('confi',confidences)
                if confidences:
                    face_max_index = np.argmax(confidences)
                if np.size(faces) == 0:
                    arduino.sendData([0, 0])
                # age 초기화
                min_age_index_final = 2
                for i, face in enumerate(faces):
                    (startX,startY) = face[0],face[1]
                    (endX,endY) = face[2],face[3]
                    (centerX, centerY) = (startX+endX)/2 , (startY+endY)/2
                    if i == face_max_index:
                        print(centerX,centerY)
                        if centerX < 100:
                            centerX = 100
                        if centerY < 100:
                            centerY = 100
                        arduino.sendData([centerX, centerY])
                    face_img = im[startY:endY, startX:startY].copy()
                    age_index_final = 2
                    if np.size(face_img) != 0:
                        blob = cv2.dnn.blobFromImage(face_img, scalefactor=1, size=(227, 227),
                            mean=(78.4263377603, 87.7689143744, 114.895847746),
                            swapRB=False, crop=False)
                        age_net.setInput(blob)
                        age_preds = age_net.forward()
                        age_index = age_preds[0].argmax()
                        if 0 <= age_index <= 1:
                            age_index_final = 0
                        if 2 <= age_index <= 3:
                            age_index_final = 1
                        if 4 <= age_index:
                            age_index_final = 2
                    if min_age_index_final > age_index_final:
                        min_age_index_final = age_index_final
                    age = age_list_final[min_age_index_final]
                    overlay_text = '%s' % (age)
                    cv2.putText(im, overlay_text, org=(startX + 100, endY), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=1, color=(255,0,0), thickness=2)
                    # draw rectangle over face
                    cv2.rectangle(im, (startX,startY), (endX,endY), (0,255,0), 2) # 검출된 얼굴 위에 박스 그리기
                    face_crop = np.copy(im[startY:endY, startX:endX])        
                    # gender detection (성별 검출)
                    if np.size(face_crop) != 0:
                        (label, confidence) = cv.detect_gender(face_crop)        
                        idx = np.argmax(confidence)
                        label = label[idx]
                        label = "{}: {:.2f}%".format(label, confidence[idx] * 100)
                        if label[:4] == 'male':
                            both_gender['male'] = 1
                        else:
                            both_gender['female'] = 1
                        Y = startY - 10 if startY - 10 > 10 else startY + 10        
                        cv2.putText(im, label, (startX, Y),  cv2.FONT_HERSHEY_SIMPLEX,
                                    0.7, (0, 255, 0), 2) # 박스 위에 남자인지 여자인지 라벨과 확률 쓰기
                cv2.imshow('result.jpg', im) # 이미지 쓰기
                skip_index = skip_index+1
                if len(faces) == 0:
                    no_face_count += 1
                    if no_face_count > 60:
                        ondisplay = 0
                        cv2.imshow('window', black)
                else:
                    ondisplay = 1
                    no_face_count = 0
                if ondisplay == 1:
                    if skip_index % 30 == 0:
                        if TIME == 0:
                            if len(faces) == 0:
                                cv2.imshow('window', img0)
                            elif len(faces) == 1:
                                if label[:4] == 'male':
                                    label = 0
                                    if min_age_index_final == 0:
                                        with open("INFO.csv", "a+", encoding="UTF-8") as f:
                                            msg = f"{now.strftime('%Y-%m-%d %H:%M:%S')},{TIME},{len(faces)},{label},{min_age_index_final}\n"
                                            f.write(msg)
                                        cv2.imshow('window', img11)
                                    elif min_age_index_final == 1:
                                        cv2.imshow('window', img12)
                                        with open("INFO.csv", "a+", encoding="UTF-8") as f:
                                            msg = f"{now.strftime('%Y-%m-%d %H:%M:%S')},{TIME},{len(faces)},{label},{min_age_index_final}\n"
                                            f.write(msg)
                                    else:
                                        cv2.imshow('window', img13)
                                        with open("INFO.csv", "a+", encoding="UTF-8") as f:
                                            msg = f"{now.strftime('%Y-%m-%d %H:%M:%S')},{TIME},{len(faces)},{label},{min_age_index_final}\n"
                                            f.write(msg)
                                # 여자일 때
                                else:
                                    label = 1
                                    if min_age_index_final == 0:
                                        with open("INFO.csv", "a+", encoding="UTF-8") as f:
                                            msg = f"{now.strftime('%Y-%m-%d %H:%M:%S')},{TIME},{len(faces)},{label},{min_age_index_final}\n"
                                            f.write(msg)
                                        cv2.imshow('window', img14)
                                    elif min_age_index_final == 1:
                                        with open("INFO.csv", "a+", encoding="UTF-8") as f:
                                            msg = f"{now.strftime('%Y-%m-%d %H:%M:%S')},{TIME},{len(faces)},{label},{min_age_index_final}\n"
                                            f.write(msg)
                                        cv2.imshow('window', img15)
                                    else:
                                        with open("INFO.csv", "a+", encoding="UTF-8") as f:
                                            msg = f"{now.strftime('%Y-%m-%d %H:%M:%S')},{TIME},{len(faces)},{label},{min_age_index_final}\n"
                                            f.write(msg)
                                        cv2.imshow('window', img16)
                            # 두 명일 때
                            elif len(faces) == 2:
                                # 남 일때
                                if both_gender['male'] == 1 and both_gender['female'] == 0:
                                    label = 0
                                    if min_age_index_final == 0:
                                        with open("INFO.csv", "a+", encoding="UTF-8") as f:
                                            msg = f"{now.strftime('%Y-%m-%d %H:%M:%S')},{TIME},{len(faces)},{label},{min_age_index_final}\n"
                                            f.write(msg)
                                        cv2.imshow('window', img17)
                                    elif min_age_index_final == 1:
                                        with open("INFO.csv", "a+", encoding="UTF-8") as f:
                                            msg = f"{now.strftime('%Y-%m-%d %H:%M:%S')},{TIME},{len(faces)},{label},{min_age_index_final}\n"
                                            f.write(msg)
                                        cv2.imshow('window', img18)
                                    else:
                                        with open("INFO.csv", "a+", encoding="UTF-8") as f:
                                            msg = f"{now.strftime('%Y-%m-%d %H:%M:%S')},{TIME},{len(faces)},{label},{min_age_index_final}\n"
                                            f.write(msg)
                                        cv2.imshow('window', img19)
                                # 둘다 여
                                elif both_gender['male'] == 0 and both_gender['female'] == 1:
                                    label = 1
                                    if min_age_index_final == 0:
                                        with open("INFO.csv", "a+", encoding="UTF-8") as f:
                                            msg = f"{now.strftime('%Y-%m-%d %H:%M:%S')},{TIME},{len(faces)},{label},{min_age_index_final}\n"
                                            f.write(msg)
                                        cv2.imshow('window', img20)
                                    elif min_age_index_final == 1:
                                        with open("INFO.csv", "a+", encoding="UTF-8") as f:
                                            msg = f"{now.strftime('%Y-%m-%d %H:%M:%S')},{TIME},{len(faces)},{label},{min_age_index_final}\n"
                                            f.write(msg)
                                        cv2.imshow('window', img21)
                                    else:
                                        with open("INFO.csv", "a+", encoding="UTF-8") as f:
                                            msg = f"{now.strftime('%Y-%m-%d %H:%M:%S')},{TIME},{len(faces)},{label},{min_age_index_final}\n"
                                            f.write(msg)
                                        cv2.imshow('window', img22)
                                # 둘다 남자이거나 여자일 때
                                else:
                                    label = 2
                                    if min_age_index_final == 0:
                                        with open("INFO.csv", "a+", encoding="UTF-8") as f:
                                            msg = f"{now.strftime('%Y-%m-%d %H:%M:%S')},{TIME},{len(faces)},{label},{min_age_index_final}\n"
                                            f.write(msg)
                                        cv2.imshow('window', img23)
                                    elif min_age_index_final == 1:
                                        with open("INFO.csv", "a+", encoding="UTF-8") as f:
                                            msg = f"{now.strftime('%Y-%m-%d %H:%M:%S')},{TIME},{len(faces)},{label},{min_age_index_final}\n"
                                            f.write(msg)
                                        cv2.imshow('window', img24)
                                    else:
                                        with open("INFO.csv", "a+", encoding="UTF-8") as f:
                                            msg = f"{now.strftime('%Y-%m-%d %H:%M:%S')},{TIME},{len(faces)},{label},{min_age_index_final}\n"
                                            f.write(msg)
                                        cv2.imshow('window', img25)
                            # 세 명일 때
                            else:
                                label = 2
                                with open("INFO.csv", "a+", encoding="UTF-8") as f:
                                            msg = f"{now.strftime('%Y-%m-%d %H:%M:%S')},{TIME},{len(faces)},{label},{min_age_index_final}\n"
                                            f.write(msg)
                                cv2.imshow('window', img26)


                    ###############

                        if TIME == 1:
                            if len(faces) == 0:
                                cv2.imshow('window', img0)
                            elif len(faces) == 1:
                                if label[:4] == 'male':
                                    if min_age_index_final == 0:
                                        with open("INFO.csv", "a+", encoding="UTF-8") as f:
                                            msg = f"{TIME},{len(faces)},{label[:4]},{min_age_index_final}\n"
                                            f.write(msg)
                                        cv2.imshow('window', img27)
                                    elif min_age_index_final == 1:
                                        cv2.imshow('window', img28)
                                    else:
                                        cv2.imshow('window', img29)
                                # 여자일 때
                                else:
                                    if min_age_index_final == 0:
                                        cv2.imshow('window', img30)
                                    elif min_age_index_final == 1:
                                        cv2.imshow('window', img31)
                                    else:
                                        cv2.imshow('window', img32)
                            # 두 명일 때
                            elif len(faces) == 2:
                                print('두명입니다')
                                # 남 일때
                                if both_gender['male'] == 1 and both_gender['female'] == 0:
                                    if min_age_index_final == 0:
                                        cv2.imshow('window', img33)
                                    elif min_age_index_final == 1:
                                        cv2.imshow('window', img34)
                                    else:
                                        cv2.imshow('window', img35)
                                # 둘다 여
                                elif both_gender['male'] == 0 and both_gender['female'] == 1:
                                    if min_age_index_final == 0:
                                        cv2.imshow('window', img36)
                                    elif min_age_index_final == 1:
                                        cv2.imshow('window', img37)
                                    else:
                                        cv2.imshow('window', img38)
                                # 둘다 남자이거나 여자일 때
                                else:
                                    if min_age_index_final == 0:
                                        cv2.imshow('window', img39)
                                    elif min_age_index_final == 1:
                                        cv2.imshow('window', img40)
                                    else:
                                        cv2.imshow('window', img41)
                            # 세 명일 때
                            else:
                                cv2.imshow('window', img42)


            ##########

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()
            msg = f"프로그램이 종료되었습니다."
            with open('INFO.csv', 'rb') as f:
                master_bot.send_document(master_mc, document=f)
            master_bot.sendMessage(master_mc,msg)

            data = pd.read_csv('INFO.csv')
            male = 0
            female = 0
            both = 0
            for d in data['sex']:
                if d==0:
                    male += 1
                elif d==1:
                    female += 1
                else:
                    both += 1
            plt.figure(1)
            plt.bar(['male', 'female', 'both'], [male, female, both])
            plt.savefig('data.png')
            baby = 0
            teen = 0
            old = 0
            for d in data['age']:
                if d==0:
                    baby+=1
                elif d==1:
                    teen+=1
                else:
                    old+=1
            plt.figure(2)
            plt.bar(['0, 6','8, 20','25, 100'], [baby, teen, old])
            plt.savefig('data2.png')
            with open('data.png', 'rb') as f:
                master_bot.send_document(master_mc, document=f)
            with open('data2.png', 'rb') as f:
                master_bot.send_document(master_mc, document=f)
        # Sensor
        if val.decode()[:len(val)-2] == '9':
            msg = f"센서가 실행됩니다"
            master_bot.sendMessage(master_mc,msg)
            stop_signal = 0
            def handler(update, context):
                global stop_signal
                user_text = update.message.text # 사용자가 보낸 메세지를 user_text 변수에 저장합니다.
                if user_text == "stop":
                    stop_signal = 1
                    master_bot.send_message(chat_id=master_mc, text="stopping sensor") # 답장 보내기
                if user_text == "help":
                    master_bot.send_message(chat_id=master_mc, text="stop 을 입력하면 카메라 종료\nstop 를 입력하면 sensor 종료 ") # 답장 보내기
            echo_handler = MessageHandler(Filters.text, handler)
            dispatcher.add_handler(echo_handler)
            cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
            img0 = cv2.imread('0.jpg')
            img1 = cv2.imread('1.jpg')
            img2 = cv2.imread('2.jpg')
            img3 = cv2.imread('3.jpg')
            img4 = cv2.imread('4.jpg')
            while True:
                if stop_signal == 1:
                    break
                if ser.readable():
                    val = ser.readline()
                    print(val.decode()[:len(val)-2])
                    if val.decode()[:len(val)-2] == '9':
                        break
                    if val.decode()[:len(val)-2] == '1':
                        onoff = 1
                    if val.decode()[:len(val)-2] == '0':
                        onoff = 0
                        cv2.imshow('window', black)
                    # print(val.decode()[:len(val)-2])
                    if onoff:
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
                        # if val.decode()[:len(val)-2] == '8':
                        #     img0 = img4
                        #     cv2.imshow('window', img4)
                        # if val.decode()[:len(val)-2] == '9':
                        #     img0 = img4
                        #     cv2.imshow('window', img4)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                    # print(val.decode()[:len(val)-2])  # 넘어온 데이터 중 마지막 개행문자 제외
            cv2.destroyAllWindows()