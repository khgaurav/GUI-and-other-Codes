
import numpy as np
import cv2

cap = cv2.VideoCapture('rtsp://192.168.1.90/user=root&password=mrm&channel=1&stream=0.sdp?real_stream--rtp-caching=1')

while(True):
    ret, frame = cap.read()
    cv2.flip(frame,1)
    cv2.imshow('Feed1',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
