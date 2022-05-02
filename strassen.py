# Kyle Ryan
# CISC 5825 Computer Algorithms
# Professor Josephine Altzman

import numpy as np

# Splitting our Matrix into Quarters
# This Results in Four Smaller Matrices 
def split(m):
    row, col = m.shape
    row2, col2 = row//2, col//2
    return(m[:row2, :col2], m[:row2, col2:], m[row2:, :col2], m[row2:, col2:])

# Strassen's Matrix Multiplication Algorithm
# Note: The Algorithm Multiplies Two Matricies of Order n, where n is a Power of 2 ex. [2, 4, 8, 16, ...]
# Additional Modifications Would Need to be Made to Pad the Matrix to Block Matrix Identity
def strassen(x, y):

    # 1x1 is Our Base Case, We can Just Multiply the Two Numbers
    if len(x) == 1:
        return(x * y)
    
    # Here We Call Split Once for Each Input
    # This Creates 8 Sub-Matricies
    a, b, c, d = split(x)
    e, f, g, h = split(y)

    # Strassen's Matrix Equation
    p1 = strassen(a, f - h)
    p2 = strassen(a + b, h)
    p3 = strassen(c + d, e)
    p4 = strassen(d, g - e)
    p5 = strassen(a + d, e + h)
    p6 = strassen(b - d, g + h)
    p7 = strassen(a - c, e + f)

    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p1 + p5 - p3 - p7

    # Combine into Our Final Matrix and Return
    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
    return(c)

array1 = np.matrix('5 5; 5 5')
array2 = np.matrix('2 2; 2 2')
print('\n' + 'Input : ')
print(str(array1) + '\n' + str(array2))
print('\n' + 'Output: ')
print(strassen(array1, array2))

array1 = np.random.randint(1, 10,size=(8,8))
array2 = np.random.randint(1, 10,size=(8,8))
print('\n' + 'Input : ')
print(str(array1) + '\n' + str(array2))
print('\n' + 'Output: ')
print(strassen(array1, array2))

'''
array1 = np.random.randint(1, 10,size=(256,256))
array2 = np.random.randint(1, 10,size=(256,256))
print('\n' + 'Input : ')
print(str(array1) + '\n' + str(array2))
print('\n' + 'Output: ')
print(strassen(array1, array2))
'''

# Another Method for Constructing a Matrix
array1 = np.matrix([[ 1, 2, 3, 4],[ 4, 5, 6, 7], [5, 6, 7, 8], [3, 2, 1, 4]])
array2 = np.matrix([[ 1, 2, 3, 4],[ 4, 5, 6, 7], [5, 6, 7, 8], [3, 2, 1, 4]])
print('\n' + 'Input : ')
print(str(array1) + '\n' + str(array2))
print('\n' + 'Output: ')
print(strassen(array1, array2))