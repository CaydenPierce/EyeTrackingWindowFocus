import cv2
from GazeTracking.gaze_tracking import GazeTracking
from i3if import i3focus
import numpy as np

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

def main():
    focus = i3focus()
    state = 'left'
    counter = 0
    
    while True:
        counter += 1
        # We get a new frame from the webcam
        _, frame = webcam.read()

        # We send this frame to GazeTracking to analyze it
        gaze.refresh(frame)

        frame = gaze.annotated_frame()
        text = ""

        if gaze.is_blinking():
            text = "Blinking"
        elif gaze.is_right():
            text = "Looking right"
        elif gaze.is_left():
            text = "Looking left"
            if state != 'left':
                focus.on_eye_change(1)
                state = 'left'
        elif gaze.is_center():
            text = "Looking center"
            if state != 'center':
                focus.on_eye_change(0)
                state = 'center'
           
if __name__ == "__main__":
    main()
