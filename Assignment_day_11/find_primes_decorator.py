from performance_log import performance_log
from Timer import Timer

def is_prime(val):
    if val<2: return False
    for i in range(2, val):
        if val%i == 0: return False
    return val

def primes_in_range(min, max=None):
    if not max: 
        max = min
        min = 1
    for val in range(min, max+1):
        if is_prime(val):
            yield val

@performance_log
def find_primes(min, max=None):
    return [x for x in primes_in_range(min, max)]


def main():
    # x = find_primes(1000)
    # print(x)
    # print(len(x))

    t = Timer()
    with t:
        p = find_primes(2, 20000)
        print('total primes: ', len(p))
    print('total time taken', t.time_taken)

if __name__ == '__main__':
    main()
