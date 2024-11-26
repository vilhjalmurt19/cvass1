import cv2
from display import VideoCapture
from fpscounter import FPSCounter
import time

def main():
    video_capture = VideoCapture('http://192.168.50.132:4747/video')
    fps_counter = FPSCounter()
    total_processing_time = 0
    frame_count = 0

    try:
        while True:
            start_time = time.time()  

            frame = video_capture.get_frame()

            #frame = video_capture.mark_brightest_spot(frame)
            frame = video_capture.mark_reddest_spot_loop(frame)
            frame = fps_counter.show(frame)

            cv2.imshow('Video', frame)

            processing_time = time.time() - start_time  
            total_processing_time += processing_time
            frame_count += 1

            print(f"Processing time for one frame: {processing_time:.4f} seconds")

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except KeyboardInterrupt:
        if frame_count > 0:
            average_processing_time = total_processing_time / frame_count
            print(f"Average processing time: {average_processing_time:.4f} seconds")
    finally:
        video_capture.release()

if __name__ == "__main__":
    main()
