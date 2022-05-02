# Kyle Ryan
# CISC 5825 Computer Algorithms
# Professor Josephine Altzman

import math

# Generic Modular Exponeniation Function
def modexp(x, y, N):
    if y == 0:
        return 1
    z = modexp(x, math.floor(y//2), N)
    return ((z**2)%N) if y % 2 == 0 else (x*(z**2)%N)

# Modular Exponentiation Calculator
def modexpcalc(base1, exp1, base2, exp2, mod):
    return((modexp(base1, exp1, mod)) - (modexp(base2, exp2, mod)))

print(modexpcalc(4, 1536, 9, 4824, 35))
print(modexpcalc(4, 1536, 9, 4824, 37))

#print(modexp(5, 5, -5))
# Testing
'''
print('+ ----------------------- +')
print((modexp(4, 1536, 35)) - (modexp(9, 4824, 35)))
print(((4**1536)-(9**4824))%35)
print('+ ----------------------- +')
print((modexp(4, 1536, 37)) - (modexp(9, 4824, 37)))
print(((4**1536)-(9**4824))%37)
'''