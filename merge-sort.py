# Kyle Ryan
# CISC 5825 Computer Algorithms
# Professor Josephine Altzman

import random

randomList = []
def randomListGenerator(start, finish, number):
    for _ in range(number):
        randomList.append(random.randint(start, finish))
    return randomList

def mergeSort(arr):
    # Exit if Arr Can't be Sorted
    if len(arr) <= 1:
        return
    
    # Set Mid, Left, and Right of Array
    mid = len(arr)//2
    l = arr[:mid]
    r = arr[mid:]

    # Sorting Left
    mergeSort(l)

    # Sorting Right
    mergeSort(r)

    i = j = k = 0

    # Creating Two Temporary Arrays for the Left and Right Side
    # i Iterates Left
    # j Iterates Right
    # k iterates Arr
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1

    while i < len(l):
        arr[k] = l[i]
        i += 1
        k += 1

    while j < len(r):
        arr[k] = r[j]
        j += 1
        k += 1

randomListGenerator(1, 25, 10)
print(f'Unsorted List: {str(randomList)}')
mergeSort(randomList)
print(f'Sorted List: {str(randomList)}')