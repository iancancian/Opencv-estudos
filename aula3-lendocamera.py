import cv2
import numpy as np

cap = cv2.VideoCapture(0) # 0 captura a webcam

while True:
    # coletar frame por frame da webcam
    _, frame = cap.read()

    cv2.imshow('Euzinhoooo', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'): # 'q' para sair 
        break