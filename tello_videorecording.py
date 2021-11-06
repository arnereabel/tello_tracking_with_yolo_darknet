import cv2


def videoRecorder():
    #create a VideoWrite object, recording to ./video.avi
    height, width, _ = frame_read.frame.shape
    video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keepRecording:
        video.write(frame_read.frame)
        time.sleep(1/30)

    video.release()

recorder = Thread(target=videoRecorder)
recorder.start()

keepRecording = False
recorder.join()
