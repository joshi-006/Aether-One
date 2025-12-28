from collections import deque
import time

WINDOW = 10
buffer = deque()

def fuse_event(event):
    buffer.append(event)
    now = time.time()

    while buffer and now - buffer[0]["timestamp"] > WINDOW:
        buffer.popleft()

    return list(buffer)
