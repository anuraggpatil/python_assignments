import time
from performance import performance_monitor
from cache import cached

@cached
@performance_monitor
def factorial(n):
    fn = 1
    for i in range(1, n+1):
        time.sleep(0.5)
        fn *= i
    return fn

def main():
    r1 = factorial(5) 

    r2 = factorial(7)

    r3 = factorial(5)

if __name__ == '__main__':
    main()