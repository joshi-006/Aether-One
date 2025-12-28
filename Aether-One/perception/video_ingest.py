import cv2
import time

def ingest_video(stream):
    cap = cv2.VideoCapture(stream)
    last = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if time.time() - last > 2:
            yield {
                "type": "video",
                "objects": ["smoke"],
                "timestamp": time.time()
            }
            last = time.time()
