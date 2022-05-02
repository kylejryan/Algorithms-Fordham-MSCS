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

def matrixMultiply(x, y):
    # 1x1 is Our Base Case, We can Just Multiply the Two Numbers
    if len(x) == 1:
        return(x * y)
    
    # Here We Call Split Once for Each Input
    # This Creates 8 Sub-Matricies
    a, b, c, d = split(x)
    e, f, g, h = split(y)

    # Normal Matrix Equation
    p1 = matrixMultiply(a, e)
    p2 = matrixMultiply(b, g)
    p3 = matrixMultiply(a, f)
    p4 = matrixMultiply(b, h)
    p5 = matrixMultiply(c, e)
    p6 = matrixMultiply(d, g)
    p7 = matrixMultiply(c, f)
    p8 = matrixMultiply(d, h)

    c11 = p1 + p2
    c12 = p3 + p4
    c21 = p5 + p6
    c22 = p7 + p8

    # Combine into Our Final Matrix and Return
    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
    return(c)

array1 = np.matrix('5 5; 5 5')
array2 = np.matrix('2 2; 2 2')
print('\n' + 'Input : ')
print(str(array1) + '\n' + str(array2))
print('\n' + 'Output: ')
print(matrixMultiply(array1, array2))

array1 = np.random.randint(1, 10,size=(8,8))
array2 = np.random.randint(1, 10,size=(8,8))
print('\n' + 'Input : ')
print(str(array1) + '\n' + str(array2))
print('\n' + 'Output: ')
print(matrixMultiply(array1, array2))

'''
array1 = np.random.randint(1, 10,size=(256,256))
array2 = np.random.randint(1, 10,size=(256,256))
print('\n' + 'Input : ')
print(str(array1) + '\n' + str(array2))
print('\n' + 'Output: ')
print(matrixMultiply(array1, array2))
'''

# Another Method for Constructing a Matrix
array1 = np.matrix([[ 1, 2, 3],[ 4, 5, 6], [5, 6, 7]])
array2 = np.matrix([[ 1, 2, 3],[ 4, 5, 6], [5, 6, 7]])
print('\n' + 'Input : ')
print(str(array1) + '\n' + str(array2))
print('\n' + 'Output: ')
print(matrixMultiply(array1, array2))