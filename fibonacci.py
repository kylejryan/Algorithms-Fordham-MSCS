# Kyle Ryan
# CISC 5825 Computer Algorithms
# Professor Josephine Altzman

# Recursive Fibonacci Sequence
def recursiveFib(n):
    # Filtering Invalid Inputs
    if type(n) != int or n < 0:
        return("Sorry, Not a Valid Input!")

    if n == 0:
        return 0
    if n == 1:
        return 1
    return recursiveFib(n - 1) + recursiveFib(n - 2)


#Iterative Fibonacci Sequence
def iterativeFib(n):
    # Filtering Invalid Inputs
    if type(n) != int or n < 0:
        return("Sorry, Not a Valid Input!")

    ultimate = 0
    current = 1
    i = 1
    while i < n:
        penultimate = ultimate
        ultimate = current
        current = penultimate + ultimate
        i += 1
    return current


# Closed Form Fibonacci Sequence
# Solution Based on: http://mathonline.wikidot.com/a-closed-form-of-the-fibonacci-sequence
def closedFormFib(n):
    # n Exists in the Series Provided in Theorum I
    try:
        if n < 0:
            return("Sorry, the Number is Not in the Series!")
        closedFormEq = (1/(5 ** 0.5)) * ( (((1+(5 ** 0.5))/2)**n) - (((1-(5 ** 0.5))/2)**n) )
        return int(closedFormEq)
    except:
        return("Sorry, Not a Valid Input!")


print(recursiveFib(100))
print(iterativeFib(0))
print(closedFormFib(0))

# Test Cases
# Invalid Inputs
'''
print(recursiveFib(-1))
print(recursiveFib(5.5))
print(recursiveFib('5'))

print(iterativeFib(-1))
print(iterativeFib(5.5))
print(iterativeFib('5'))

print(closedFormFib(-1))
print(closedFormFib(5.5))
print(closedFormFib('5'))
'''