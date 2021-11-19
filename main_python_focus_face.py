import cv2
import time
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject

cap = cv2.VideoCapture(0)
detector = FaceDetector()
arduino = SerialObject()

while True:
    # time.sleep(0.1)
    success, img = cap.read()
    if success:
        img, bboxs = detector.findFaces(img)

        if bboxs:
            print(bboxs[0]['center'])
            arduino.sendData([bboxs[0]['center'][0], bboxs[0]['center'][1]])
        else:
            arduino.sendData([0, 0])
        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()