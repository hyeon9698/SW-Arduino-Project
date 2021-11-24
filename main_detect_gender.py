# import libraries
import cv2
import cvlib as cv
import numpy as np
import dlib
from cvzone.SerialModule import SerialObject

cap = cv2.VideoCapture(0)
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
while True:
    success, im = cap.read()
    faces, confidences = cv.detect_face(im)
    for face in faces:
        (startX,startY) = face[0],face[1]
        (endX,endY) = face[2],face[3]
        (centerX, centerY) = (startX+endX)/2 , (startY+endY)/2
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
        (label, confidence) = cv.detect_gender(face_crop)        
        idx = np.argmax(confidence)
        label = label[idx]
        label = "{}: {:.2f}%".format(label, confidence[idx] * 100)
        Y = startY - 10 if startY - 10 > 10 else startY + 10        
        cv2.putText(im, label, (startX, Y),  cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (0, 255, 0), 2) # 박스 위에 남자인지 여자인지 라벨과 확률 쓰기
    cv2.imshow('result.jpg', im) # 이미지 쓰기
    print(label)
    if label[:4] == 'male':
        cv2.imshow('window', img1)
    else:
        cv2.imshow('window', img2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()