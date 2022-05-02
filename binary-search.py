import random

# NOT WORKING!!
# Random List Generator and Sorter
list = []
def randomList(start, finish, number):
    for _ in range(number):
        list.append(random.randint(start, finish))
    list.sort()
    return list


# Binary Search

counter = [0]
def binarySearch(arr, l, r, x):
    counter[0] += 1
    try:
        if r >= 1:

            mid = 1 + (r - l) // 2

            if arr[mid] == x:
                return mid

            elif arr[mid] > x:
                return(binarySearch(arr, l, mid - 1, x))

            else:
                return(binarySearch(arr, mid + 1, r, x))

        else:
            return('Not Found.')
    except Exception:
        return('Not Found.')


x = 5

randomList(0, 10, 10)
print(list)

print(binarySearch(list, 0, len(list)-1, x))
print(counter[0])