import cv2 as cv



# #to read images and return them as matrix of rgb each pixel has 3 values rgb

img = cv.imread('Resources\Photos\cat_large.jpg')
cv.imshow('cat', img) #displays the images in a new window and the matrix of pixels of image to display
cv.waitKey(0)


#READING VIDEOS
capture = cv.VideoCapture('Resources\Videos\dog.mp4') #to read live videos/recorded vids, instance of videoCapture class
while True:
    isTrue, frame = capture.read()
    #reads video frame by frame, returns the frame and returns the boolean that denotes whether the frame was read or not
    cv.imshow('Video', frame)

    if( cv.waitKey(1) & 0xFF == ord('d')): #waitKey(1) somehow defines the speed of video to be played
        #as it denotes the duration for which each frame of the video is to be displayed4
        break

#-215:Assertion failed -> file(image) not found or all the frames in the video have been read
capture.release()
cv.destroyAllWindows()