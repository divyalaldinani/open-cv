import cv2 as cv
import numpy as np


img = cv.imread('Resources/Photos/cats.jpg')
# cv.imshow('cats', img)
x = img[0][0][0]
print(type(x)) #data type - numpy.uint8 i.e., int 8 contains digits from 0 to 255 thus 8 bits are enough
# cv.waitKey(0)

blank = np.zeros((500, 800, 3), dtype = 'uint8')
blank[250:500, 0:250] = (40, 120, 240)


cv.circle(blank, (250, 250), 200,  (240, 120, 40), thickness = -1)
cv.rectangle(blank, (200, 200), (400, 600), (255, 4, 255), thickness = -1)
# cv.rectangle()
cv.line(blank, (0, 0), (blank.shape[1], blank.shape[0]), (80, 80, 250), thickness=2)
cv.imshow('blank', blank)
cv.waitKey(0)


cv.putText(blank, "Hey, ig i am happy", (100, 100), cv.FONT_HERSHEY_COMPLEX, 1.0, (80, 0, 230), thickness= 1)
cv.imshow("Text window", blank)
cv.waitKey(0)
