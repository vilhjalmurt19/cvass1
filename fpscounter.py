import time
import cv2

class FPSCounter:
    def __init__(self):
        self.start_time = time.time()
        self.frame_count = 0
    
    def update(self):
        self.frame_count += 1
        elapsed_time = time.time() - self.start_time
        if elapsed_time > 0:
            fps = self.frame_count / elapsed_time
        else:
            fps = 0
        return fps

    def show(self, frame):
        fps = self.update()
        cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        return frame

    def reset(self):
        self.start_time = time.time()
        self.frame_count = 0