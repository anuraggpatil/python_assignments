import time
def performance_log(fn_target):
    def inner(*args, **kwargs):
        start_time = time.time()
        result = [x for x in fn_target(*args, **kwargs)]  
        end_time = time.time()
        time_taken = end_time-start_time
        print(f'time taken: {time_taken}sec')
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

x = find_primes(1000)
print(x)
print(len(x))
            