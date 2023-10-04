
class prime_range:
    def __init__(self, min, max):
        self._min = min
        self._max = max
    
    def __iter__(self):
        return self.range_iterator(self._min, self._max)
    
    def is_prime(val):
        if val<2: return 
        for i in range(2, val):
            if val%i == 0: return 
        return val

    class range_iterator:
        def __init__(self, min, max):
            self._max = max
            self._val = min-1

        def __next__(self):
            self._val += 1
            if self._val <= self._max:
                if not prime_range.is_prime(self._val):
                    self.__next__()
                return prime_range.is_prime(self._val)
            else:
                raise StopIteration()
            
for p in prime_range(10, 20):
    print(p, end=' ')
print()
primes= prime_range(10,20)
it=iter(primes)
print(next(it)) #11
print(next(it)) #13
print(next(it)) #17
print(next(it)) #19
# print(next(it)) # raises StopIteration