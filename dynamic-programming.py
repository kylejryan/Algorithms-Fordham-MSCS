# Kyle Ryan
# CISC 5825 Computer Algorithms
# Professor Josephine Altzman

import sys

# Function to Find Max Sub Array Sum
def maxSubArray(A):

    # Sets Local Max to Zero and Global Max to -Inf
    local_max = 0
    global_max = -sys.maxsize - 1

    # Iterate Through A
    for i in range(len(A)):
        # Find the Local Max Sub Array
        local_max = max(A[i], A[i] + local_max)

        #If Greater Than Global, Set Global to Local
        if local_max > global_max:
            global_max = local_max

    # Return Global
    return global_max

array1 = [5, 15, -30, 10, -5, 40, 10]
array2 = [-5, -10, -5, -30, -50, -60]
array3 = [5, 10, 15, 20, 25, 30]

# Expected Value: 55
print(maxSubArray(array1))

# Expected Value: -5
print(maxSubArray(array2))

# Expected Value: 105
print(maxSubArray(array3))