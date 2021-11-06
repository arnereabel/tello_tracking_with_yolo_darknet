from djitellopy import Tello
import cv2
import time
from threading import Thread



tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()


tello.get_battery()
cv2.imwrite('picture.png', frame_read.frame)
tello.get_battery()

tello.streamoff()




keeprecording  = True    # while keeprecording is True , continue reading frames

tello.streamon()
frame_read = tello.get_frame_read()


def videoRecorder():
    #create a VideoWrite object, recording to ./video.avi
    height, width, _ = frame_read.frame.shape
    video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keeprecording:
        video.write(frame_read.frame)
        time.sleep(1/30)

    video.release()

recorder = Thread(target=videoRecorder)
recorder.start()

tello.get_battery()
time.sleep(50)
tello.get_battery()

keepRecording = False
recorder.join()
