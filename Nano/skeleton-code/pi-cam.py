import cv2
print(cv2.__version__)

dispW = 640     # display width (in pixel)
dispH = 480     # display height (in pixel)
flip = 2        # orientation of pi 2 camera 
                # 0 = upside down, 1 = clockwise rotation 1x,
                # 2 = clockwise rotation 2x (correct orientation), 
                # 3 = clockwise roation 3x 
# string variable for camera setting
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# nvarguscamerasrc = launches GStreamer
# video/x-raw(memory:NVMM) = video format
# width=3264, height=2464 = native resolution (width and height) of what is coming FROM the pi 2 camera
# format=NV12, framerate=21/1 = format of incoming image at 21 FPS
# nvvidconv flip-method='+str(flip)+ = nvidia conversion flip method
# ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+' = video output format with specified resolution

cam = cv2.VideoCapture(camSet)  # camera object (cam) - Pi camera

# camera/video is a 1 frame and 1 frame and we want to continuously capture each frame 
while(True):
    ret, frame = cam.read()     
    # when you read a frame, first is usually a 0 or 1 indicating if you got a frame or not (ret)
    # frame = image itself. this will grab the latest frame
    # we need to have it settup to catch two variable. we rearly be using the first variable (ret). so ignore that - just a place holder
    
    cv2.imshow("PI_CAM",frame)  
    # parameter1 = show in window call "PI_Cam"
    # parameter2 = what am i gonna show in that window? --> frame variable (actual capture)
    # if you have a program running and not properly close it then it may have unfinished business
    # we have gone out and created a window and locked up the camera. if we kill the program then it might have issue
    # THUS, need a proper way to kill the program and clean-up (gracefully exit) - we setup a KEY
    
    if(cv2.waitKey(1) == ord("q")):  # goes out for 1ms to see if there a key being pressed (q). ord = ordinates of the key
        break

cam.release()
cv2.destroyAllWindows()




