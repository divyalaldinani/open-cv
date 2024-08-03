import cv2 as cv
import numpy as np

# Gray=0.299×Red+0.587×Green+0.114×Blue
# converting RGB to Grayscale

#NOTE: its not RBG its BGR in python coz [b, g, r] thats how each pixel is represented
img = cv.imread('Resources\Photos\group 2.jpg')
print(img.shape)
grayscale_matrix = np.zeros((img.shape[0], img.shape[1]), dtype = 'uint8')
cv.imshow("image", img)
# cv.imshow("gray image", grayscale_matrix)
cv.waitKey(0)


#NOTE: METHOD1
# for i in range(img.shape[0]):
#     for j in range(img.shape[1]):
#         red = img[i][j][2]
#         green = img[i][j][1]
#         blue = img[i][j][0]
#         grayscale_matrix[i][j] = (int)(0.299*red + 0.587*green + 0.114*blue)


#METHOD 2
grayscale_matrix = np.dot(img[...,:3], [0.299, 0.587, 0.114])
grayscale_matrix = grayscale_matrix.astype(np.uint8) #uint8 is 8 bit unsigned integer
cv.imshow("gray image", grayscale_matrix)
cv.waitKey(0)



grayscale_matrix = grayscale_matrix.astype(np.int8) # while int 8 is signed integer, this will just created a negative version of image


cv.imshow("gray image in negative", grayscale_matrix)
cv.waitKey(0)


#METHOD 3: USING inbuilt fns lol
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray image", gray)
cv.waitKey(0)


#BLURRING AN IMAGE using Guassian blur
#Uses a Gaussian function to weight the average of pixels around each pixel. It is effective for reducing noise and detail while preserving edges to some extent.

blurred_image = cv.GaussianBlur(img, (3, 3), cv.BORDER_REFLECT101)
cv.imshow("blurred image", blurred_image)
cv.waitKey(0)


#EDGES IN IMAGE: 
#Edges in an image refer to the boundaries between different regions or objects where there is a significant change in intensity or color. 
# They represent areas where the image's pixel values change abruptly, which often corresponds to important features or transitions in the visual scene.
#Using canny edge detector
edges = cv.Canny(img, 100, 200)
cv.imshow("image with edges", edges)
cv.waitKey(0)
#Strong Edges: Pixels with gradient values greater than threshold2 are considered strong edges. These pixels are immediately marked as edges.
# Weak Edges: Pixels with gradient values between threshold1 and threshold2 are considered weak edges. 
# To determine whether these weak edges are part of an edge, the algorithm performs edge tracking. 
# If a weak edge pixel is connected to a strong edge pixel, it is also considered an edge; otherwise, it is discarded.


# #NOTE: to reduce images we can just pass on a blurred version of image and the edges will reduce

#NOTE: READ: https://medium.com/analytics-vidhya/morphological-transformations-of-images-using-opencv-image-processing-part-2-f64b14af2a38#:~:text=Morphological%20transformations%20are%20some%20simple,decides%20the%20nature%20of%20operation.


#NOTE: from https://docs.opencv.org/3.4/d9/d61/tutorial_py_morphological_ops.html


img = cv.imread('Resources/Photos/images-morphological-transformations/j-image.png')
kernel = np.ones((5, 5), np.uint8)
erosion = cv.erode(img, kernel, iterations = 1)
cv.imshow('Original Image', img)
cv.imshow('Eroded image', erosion)
cv.waitKey(0)

dilation = cv.dilate(erosion, kernel, iterations = 1)
cv.imshow("Dilated Image", dilation)
cv.waitKey(0)


img = cv.imread('Resources/Photos/images-morphological-transformations/noised-image.png')
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel )
cv.imshow('image', img)
cv.imshow('image without noise', opening)
cv.waitKey(0)

img = cv.imread('Resources/Photos/images-morphological-transformations/closing-image.png')
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
cv.imshow('image', img)
cv.imshow('closed image', closing)
cv.waitKey(0)


img = cv.imread('Resources/Photos/images-morphological-transformations/j-image.png')
morph_gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
cv.imshow('image', img)
cv.imshow('gradient image', morph_gradient)
cv.waitKey(0)


tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
cv.imshow('top hat', tophat)
cv.waitKey(0)


blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)
cv.imshow('black hat', blackhat)
cv.waitKey(0)