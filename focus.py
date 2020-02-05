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

        look = gaze.horizontal_ratio()
        if look is not None:
            if look > 0.68 and state != "left":
                focus.on_eye_change(1)
                state = 'left'
            if look < 0.61 and state != 'right':
                focus.on_eye_change(0)
                state = "right"

           
if __name__ == "__main__":
    main()
