# Python program to find Smallest
# Number Using Stack

import math

def printSmallest(arr):

    arr_size = len(arr)
    if arr_size < 2:
        print ("Invalid Input")
        return

    first = math.inf
    for i in range(0, arr_size):

        if arr[i] < first:
            second = first
            first = arr[i]

        elif (arr[i] != first):
            second = arr[i];

    else:
        print('The smallest element is',first)

arr = [12, 13, 17, 10, 20, 15]
printSmallest(arr)
