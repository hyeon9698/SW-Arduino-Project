# import libraries
import cv2
import cvlib as cv
import numpy as np
from cvzone.SerialModule import SerialObject
from datetime import datetime, timedelta
from pytz import timezone

cap = cv2.VideoCapture(1)
arduino = SerialObject()

age_net = cv2.dnn.readNetFromCaffe(
                'models/deploy_age.prototxt', 
                'models/age_net.caffemodel')
age_list_final = ['(0, 6)','(8, 20)','(25, 100)']
cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
img0 = cv2.imread('0.jpg')
img1 = cv2.imread('1.jpg')
img2 = cv2.imread('2.jpg')
img3 = cv2.imread('3.jpg')
img4 = cv2.imread('4.jpg')
cv2.imshow('window', img0)
label = 'male'
TIME = 0 # 0 이면 낮 1이면 밤
while True:
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
    print('confi',confidences)
    if confidences:
        face_max_index = np.argmax(confidences)
    if np.size(faces) == 0:
        arduino.sendData([0, 0])
    for i, face in enumerate(faces):
        (startX,startY) = face[0],face[1]
        (endX,endY) = face[2],face[3]
        (centerX, centerY) = (startX+endX)/2 , (startY+endY)/2
        if i == face_max_index:
            print(centerX,centerY)
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
        age = age_list_final[age_index_final]
        overlay_text = '%s' % (age)
        cv2.putText(im, overlay_text, org=(startX + 100, startY), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=1, color=(255,0,0), thickness=5)
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
                both_gender['female'] = 2
            Y = startY - 10 if startY - 10 > 10 else startY + 10        
            cv2.putText(im, label, (startX, Y),  cv2.FONT_HERSHEY_SIMPLEX,
                        0.7, (0, 255, 0), 2) # 박스 위에 남자인지 여자인지 라벨과 확률 쓰기
    cv2.imshow('result.jpg', im) # 이미지 쓰기
    # print(label)
    # 한 명일 때
    if len(faces) == 1:
        if label[:4] == 'male':
            if age_index_final == 0:
                if TIME == 0:
                    cv2.imshow('window', img1)
                else:
                    pass
            elif age_index_final == 1:
                if TIME == 0:
                    cv2.imshow('window', img3)
                else:
                    pass
            else:
                if TIME == 0:
                    cv2.imshow('window', img1)
                else:
                    pass
        # 여자일 때
        else:
            if age_index_final == 0:
                if TIME == 0:
                    cv2.imshow('window', img3)
                else:
                    pass
            elif age_index_final == 1:
                if TIME == 0:
                    cv2.imshow('window', img3)
                else:
                    cv2.imshow('window', img2)
            else:
                if TIME == 0:
                    cv2.imshow('window', img1)
                else:
                    pass
    # 두 명일 때
    elif len(faces) == 2:
        print('두명입니다')
        # 남 여 일때
        if both_gender['male'] == 1 and both_gender['female'] == 1:
            if age_index_final == 0:
                if TIME == 0:
                    cv2.imshow('window', img3)
                else:
                    pass
            elif age_index_final == 1:
                if TIME == 0:
                    cv2.imshow('window', img3)
                else:
                    pass
            else:
                if TIME == 0:
                    cv2.imshow('window', img3)
                else:
                    pass
        # 둘다 남자이거나 여자일 때
        else:
            if age_index_final == 0:
                if TIME == 0:
                    cv2.imshow('window', img3)
                else:
                    pass
            elif age_index_final == 1:
                if TIME == 0:
                    cv2.imshow('window', img3)
                else:
                    pass
            else:
                if TIME == 0:
                    cv2.imshow('window', img3)
                else:
                    pass
    # 세 명일 때
    else:
        if TIME == 0:
            cv2.imshow('window', img3)
        else:
            pass

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()