import cv2 as cv

img = cv.imread('Resources\Photos\cat_large.jpg')
cv.imshow('Cat', img) #cat is the name of the window that displays the image
# print(img.shape)

def resize(frame, scale = 0.75):
    #shape: height * width
    width = (int)(frame.shape[1] * scale)
    height = (int)(frame.shape[0] * scale)
    dimensions = (width, height)
    # print(frame.shape)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img_resized = resize(img, 0.2)
cv.imshow('Resized', img_resized)
cv.waitKey(0)



capture = cv.VideoCapture('Resources\Videos\dog.mp4')
# cv.imshow(changeFrame(750, 750))
while True:
    isTrue, frame = capture.read()
    #reads video frame by frame, returns the frame and returns the boolean that denotes whether the frame was read or not
    cv.imshow('Video', resize(frame, 0.5))

    if( cv.waitKey(1) & 0xFF == ord('d')): #waitKey(1) somehow defines the speed of video to be played
        #as it denotes the duration for which each frame of the video is to be displayed4
        break 

def changeFrame(width, height): #only for live videos
    capture.set(3, width)
    capture.set(4, height)



