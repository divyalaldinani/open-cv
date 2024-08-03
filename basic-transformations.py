import cv2 as cv
import numpy as np

#translation: Shifting the image by tx pixels along the x-axis and ty pixels along the y-axis.
img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('image', img)
x = -50
y = -10
a, b, c, d = 1, 0, 0, 1
transMat = np.float32([[a, b, x],[c, d, y]])
dimensions = (img.shape[1], img.shape[0])
transformation = cv.warpAffine(img, transMat, dimensions)
cv.imshow('transformed image', transformation)
cv.waitKey(0)


# #rotation 
(height, width) = img.shape[0:2]
M = cv.getRotationMatrix2D((width//2, height//2), 45, 1 )
rotated = cv.warpAffine(img, M, (width, height))
cv.imshow('rotated', rotated)


#if we try to rotate the rotated image then it may introduce black triangles, thus its better to rotate the org image
M = cv.getRotationMatrix2D((width//2, height//2), 45, 1)
rotate_rotated = cv.warpAffine(rotated, M, (width, height))
cv.imshow('rotated image', rotate_rotated)
cv.waitKey(0)

print(img.shape)



#resizing
#shrinking: INTER_AREA
#enlarging: INTER_LINEAR, INTER_CUBIC, cubic takes time but yields better image
#Interpolation is a technique used to estimate missing or new data points within a range of known data points. 
# In image processing, it helps in generating new pixel values for operations like resizing, rotating, and 
# transforming images, ensuring that the resulting image is smooth and visually coherent.
resized = cv.resize(img, (960, 640), interpolation= cv.INTER_LINEAR)
cv.imshow("resize with linear", resized)

resized = cv.resize(img, ( 960, 640), interpolation= cv.INTER_CUBIC)
cv.imshow("resized with cubic", resized)

resized = cv.resize(img, (320, 216), interpolation=cv.INTER_AREA)
cv.imshow("resized with area", resized)
cv.waitKey(0)


#flipping
cv.imshow("original", img)
flip1 = cv.flip(img, 0) #vertical flipping
flip2 = cv.flip(img, 1) #horizontal flipping
flip3 = cv.flip(img, -1) #vertical and horizontal flipping
cv.imshow("flip1", flip1)
cv.imshow("flip2", flip2)
cv.imshow("flip3", flip3)
cv.waitKey(0)

#cropped

cropped = img[100:400, 100:500]
cv.imshow("cropped", cropped)
cv.waitKey(0)