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

def performance_log(fn_target):
    def inner(*args, **kwargs):
        start_time = time.time()
        result = [x for x in fn_target(*args, **kwargs)]  
        end_time = time.time()
        time_taken = end_time-start_time
        # print(f'time taken: {time_taken}sec')
        return result
    return inner


def is_prime(val):
    if val<2: return False
    for i in range(2, val):
        if val%i == 0: return False
    return val

@performance_log
def find_primes(min, max=None):
    if not max: 
        max = min
        min = 1
    for val in range(min, max+1):
        if is_prime(val):
            yield val

# x = find_primes(1000)
# print(x)
# print(len(x))

t = Timer()
with t:
    p = find_primes(2, 20000)
    print('total primes: ', len(p))
print('total time taken', t.time_taken)

