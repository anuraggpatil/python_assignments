import time

class Timer:
    def __init__(self):
        self.time_taken = None
        self.start = None

    def __enter__(self):
        self.start = time.time()
    
    def __exit__(self, t, e, s):
        end = time.time()
        self.time_taken = end - self.start