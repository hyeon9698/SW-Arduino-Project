# import libraries
import cv2
import cvlib as cv
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    success, im = cap.read()

    # detect faces (얼굴 검출)
    faces, confidences = cv.detect_face(im)

    for face in faces:
        (startX,startY) = face[0],face[1]
        (endX,endY) = face[2],face[3]
        # draw rectangle over face
        cv2.rectangle(im, (startX,startY), (endX,endY), (0,255,0), 2) # 검출된 얼굴 위에 박스 그리기
        face_crop = np.copy(im[startY:endY, startX:endX])
        
        # gender detection (성별 검출)
        (label, confidence) = cv.detect_gender(face_crop)
        
        print(confidence)
        print(label)
        
        idx = np.argmax(confidence)
        label = label[idx]

        label = "{}: {:.2f}%".format(label, confidence[idx] * 100)

        Y = startY - 10 if startY - 10 > 10 else startY + 10

        cv2.putText(im, label, (startX, Y),  cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (0, 255, 0), 2) # 박스 위에 남자인지 여자인지 라벨과 확률 쓰기
    cv2.imshow('result.jpg', im) # 이미지 쓰기
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break