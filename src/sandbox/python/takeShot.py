import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ret, img = cap.read()
cv2.imwrite('nao_pic.png',img)
