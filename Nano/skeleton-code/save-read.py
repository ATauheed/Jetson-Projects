#!/usr/bin/env python3

import sys
import cv2

window_title = "Logi-Cam"
WIDTH = 640
HEIGHT = 480
FPS = 30


# ASSIGN CAMERA ADDRESS HERE
camera_id = "/dev/video1"

# cam objects
# SAVING 
# comment out if reading 
        ### from here 
#video_capture = cv2.VideoCapture(camera_id, cv2.CAP_V4L2)
#out_video = cv2.VideoWriter("videos/myCam.avi", cv2.VideoWriter_fourcc(*"XVID"), FPS, (WIDTH,HEIGHT))
        ### to here

# READING
# comment out if writing
video_capture = cv2.VideoCapture("videos/myCam.avi")

# object to write video
# cv2.VideoWriter("writing_location_with_filename", format, frame_rate, (width,height))

# cam setup
video_capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'YUYV'))
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
video_capture.set(cv2.CAP_PROP_FPS, FPS)


while(True):
    ret, frame = video_capture.read()

    cv2.imshow(window_title, frame)
    cv2.moveWindow(window_title, 0, 0)

    # writing frame
    # if reading then comment the line below out
    #out_video.write(frame)  
    

    if(cv2.waitKey(1) == ord("q")):  # goes out for 1ms to see if there a key being pressed (q). ord = ordinates of the key
        break
    
    # reading from file will run the video super fast
    # work around: implement delay by modifing the if statement:
    if(cv2.waitKey(33) == ord("q")):
       break
    # 30 FPS is 33.33 ms/frame

video_capture.release()
out_video.release()     # closing the file
cv2.destroyAllWindows()