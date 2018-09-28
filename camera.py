
import numpy as np
import cv2

cap = cv2.VideoCapture('rtsp://192.168.1.10/user=admin&password=&channel=1&stream=0.sdp?real_stream--rtp-caching=100')

while(True):
    ret, frame = cap.read()
    cv2.imshow('ball',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()