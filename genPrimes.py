def genPrimes():
    primes = []
    x = 2
    while True:
        for p in primes:
            if (x % p) == 0:
                break
        else:
            primes.append(x)
            yield x
        x += 1


foo = genPrimes()
print(next(foo))
print(next(foo))
print(next(foo))
print(next(foo))
print(next(foo))
print(next(foo))
print(next(foo))
print(next(foo))
print(next(foo))
print(next(foo))
print(next(foo))
print(next(foo))

def genPrimes2():
    primes = []
    x = 2
    for i in range(60):
        for p in primes:
            if (x % p) == 0:
                break
        else:
            primes.append(x)
        x += 1
    print(primes)
        
genPrimes2()
