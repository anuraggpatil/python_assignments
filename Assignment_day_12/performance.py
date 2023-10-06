import time
def performance_monitor(fn_target):
        
    def inner(*args, **kwargs):
        start_time = time.time()
        result = fn_target(*args, **kwargs)
        end_time = time.time()
        inner.time_taken = end_time-start_time
        return result

    return inner