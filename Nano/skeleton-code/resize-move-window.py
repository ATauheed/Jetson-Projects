#!/usr/bin/env python3

import sys
import cv2

window_title = "Logi-Cam"
WIDTH = 320
HEIGHT = 240
FPS = 30


# ASSIGN CAMERA ADDRESS HERE
camera_id = "/dev/video1"
# Full list of Video Capture APIs (video backends): https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html
# For webcams, we use V4L2
video_capture = cv2.VideoCapture(camera_id, cv2.CAP_V4L2)
video_capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'YUYV'))
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
video_capture.set(cv2.CAP_PROP_FPS, FPS)


while(True):
    ret, frame = video_capture.read()
    cv2.imshow(window_title, frame)
    cv2.moveWindow(window_title, 0, 0)  # move window to a specific xy location (in pixels)

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    # convert frame to different color (gray)
    cv2.imshow("Gray_Image", gray_frame)   
    cv2.moveWindow("Gray_Image", 400, 0)

    color_frame_small = cv2.resize(frame, (160, 120))   # resize an existing frame
    cv2.moveWindow("small_frame", 0, 300)
    gray_small = cv2.resize(gray_frame, (160, 120))
    cv2.moveWindow("gray_small", 400, 300)

    
    cv2.imshow("small_frame", color_frame_small)
    cv2.imshow("gray_small", gray_small)

    # imshow and moveWindow window name needs to be same



    if(cv2.waitKey(1) == ord("q")):  # goes out for 1ms to see if there a key being pressed (q). ord = ordinates of the key
        break

video_capture.release()
cv2.destroyAllWindows()