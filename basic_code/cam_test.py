import cv2
import time

cap = cv2.VideoCapture(1)

while True:
    success, img = cap.read()
    if success:
        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()