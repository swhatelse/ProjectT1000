import cv2
import numpy as np
from matplotlib import pyplot as plt

origin = cv2.imread("P4_nao.jpg");

img_rgb = cv2.imread('nao_bin.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
img_canny = cv2.Canny(img_gray, 100, 100)

template = cv2.imread('pion.png', 0)
#template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
#template_canny = cv2.Canny(template_gray, 100, 100)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_canny,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.40

img_toDisplay = origin

loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_toDisplay, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)

#cv2.imwrite('model.png', template_canny)
#cv2.imwrite('res.png',img_rgb)

key = -1
while(key != ord('q')):
	cv2.imshow('img_gray', img_toDisplay)
	key = cv2.waitKey(20)


