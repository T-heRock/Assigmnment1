# Python Program to find the
# total count of pairs with given sum.


def getPairsCount(arr, n, sum):

    count = 0 

    
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count += 1

    return count


arr = [8, 4, 7, -1, 5]
n = len(arr)
sum = 12
print("Count of pairs is", getPairsCount(arr, n, sum))
