import numpy as np

def gauss_method(a, b):

    # Setting n to the Length of b
    n = len(b) 

    # Elimination Phase
    # Matrix Row
    for k in range(n - 1): 
        # Matrix Column
        for i in range(k + 1, n): 
                # If Row and Column != 0
                if a[i,k] != 0.0:
                    factor = a[i,k] / a[k,k]
                    a[i, k + 1: n] = a[i, k + 1: n] - np.multiply(factor, a[k, k + 1: n])
                    b[i] = b[i] - np.multiply(factor, b[k])

    # Back Substitution
    for k in range(n - 1, -1, -1):
        b[k] = (b[k] - np.dot(a[k, k + 1: n], b[k + 1: n])) / a[k, k]

    # Returning b
    return b


a = np.array([[9, 12, 10, 8, 6],
              [11, 3, 13, 7, 5],
              [14, 15, 16, 17, 18],
              [19, 20, 21, 22, 4],
              [23, 24, 25, 26, 27]], 
              dtype = float)

b = np.array([16, -60, 29, 20, 47], dtype = float)

print(gauss_method(a, b))