#!/usr/bin/env python3

import sys
import cv2

window_title = "Logi-Cam"
WIDTH = 640
HEIGHT = 480
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
""" 
# How to set video capture properties using V4L2:
# Full list of Video Capture Properties for OpenCV: https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html
#Select Pixel Format:
# video_capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'YUYV'))
# Two common formats, MJPG and H264
# video_capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
# Default libopencv on the Jetson is not linked against libx264, so H.264 is not available
# video_capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'H264'))
# Select frame size, FPS:
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
video_capture.set(cv2.CAP_PROP_FPS, 30)
"""

while(True):
    ret, frame = video_capture.read()

    cv2.imshow(window_title, frame)

    if(cv2.waitKey(1) == ord("q")):  # goes out for 1ms to see if there a key being pressed (q). ord = ordinates of the key
        break

video_capture.release()
cv2.destroyAllWindows()