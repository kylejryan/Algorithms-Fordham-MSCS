import math
import random

def modexp(x, y, N):
    if y == 0:
        return 1
    z = modexp(x, math.floor(y//2), N)
    return ((z**2)%N) if y % 2 == 0 else (x*(z**2)%N)
    

def isPrime(N):
    if N in [1, 4]:
        return False
    elif N in [2, 3]:
        return True

    else:
        for _ in range(128):
            a = random.randint(2, N-2)

            if modexp(a, N-1, N) != 1:
                return False
        return True
'''
print('\n' + '+ --------- Evaluation ---------- +')
# Magic Numbers for the Homework
magicNumbers = [
    10106665597294733930808268834911,
    557940830126698960967415391,
    2305567963945518424753102147331756071,
    169665573205075467667167
]

print('+ -------- Magic Numbers -------- +')
for item in magicNumbers:
    print(isPrime(item))

print('\n' + '+ ------------ Testing ------------ +')
# Mersenne Prime, Should be True
mersennePrimes = [
    2305843009213693951,
    618970019642690137449562111,
    162259276829213363391578010288127,
    170141183460469231731687303715884105727
]

print('+ -------- Mersenne Primes -------- +')
for item in mersennePrimes:
    print(isPrime(item))


# Carmichael Number, Should be False
carmichaelNumbers =[
    561,
    41041,
    825265,
    9746347772161
]

print('+ -------- Carmichael Numbers -------- +')
for item in carmichaelNumbers:
    print(isPrime(item))

# Small Primes, Should be True
smallPrimes = [
    2,
    11,
    73
]
print('+ -------- Small Primes -------- +')
for item in smallPrimes:
    print(isPrime(item))

# Small Composites, Should be False
smallComposites = [
    8,
    16,
    64
]
print('+ -------- Small Composites -------- +')
for item in smallComposites:
    print(isPrime(item))
'''

midtermNumbers = [671998030559713968361666935769,
282174488599599500573849980909,
284616413071054560077067628069,
521419622856657689423872613771,
72191103626161875816648846887
]
for item in midtermNumbers:
    print(isPrime(item))