import time
from performance import performance_monitor
from cache import cached

@performance_monitor
@cached
def factorial(n):
    fn = 1
    for i in range(1, n+1):
        time.sleep(0.5)
        fn *= i
    return fn

def main():
    r1 = factorial(5) 
    print(factorial.time_taken)

    r2 = factorial(7)
    print(factorial.time_taken)

    r3 = factorial(5)
    print(factorial.time_taken)

    r4 = factorial(7)
    print(factorial.time_taken)


if __name__ == '__main__':
    main()