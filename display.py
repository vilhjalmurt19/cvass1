import cv2
import numpy as np

class VideoCapture:
    def __init__(self, camera_index=0):
        self.cap = cv2.VideoCapture(camera_index)
        if not self.cap.isOpened():
            raise ValueError("Error: Could not open video stream.")

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            raise RuntimeError("Error: Can't receive frame (stream end?).")
        return frame

    def mark_brightest_spot(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(gray)
        cv2.circle(frame, max_loc, 10, (0, 255, 0), 2)  
        return frame

    def mark_reddest_spot(self, frame):
        red_channel = frame[:, :, 2]
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(red_channel)
        cv2.circle(frame, max_loc, 10, (255, 0, 0), 2)  
        return frame

    def mark_brightest_spot_loop(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        max_val = -1
        max_loc = (0, 0)
        for y in range(gray.shape[0]):
            for x in range(gray.shape[1]):
                if gray[y, x] > max_val:
                    max_val = gray[y, x]
                    max_loc = (x, y)
        cv2.circle(frame, max_loc, 10, (0, 255, 0), 2)  # Draw a green circle around the brightest spot
        return frame

    def mark_reddest_spot_loop(self, frame):
        red_channel = frame[:, :, 2]
        max_val = -1
        max_loc = (0, 0)
        for y in range(red_channel.shape[0]):
            for x in range(red_channel.shape[1]):
                if red_channel[y, x] > max_val:
                    max_val = red_channel[y, x]
                    max_loc = (x, y)
        cv2.circle(frame, max_loc, 10, (255, 0, 0), 2)  # Draw a blue circle around the reddest spot
        return frame

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()