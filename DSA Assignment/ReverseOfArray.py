# Python Program to Print the 
# Reverse of the Given Array 

def reverseList(A, start, end):
    if start >= end:
        return
    A[start], A[end] = A[end], A[start]
    reverseList(A, start+1, end-1)


A = [12,6,-7,4,3,1]
print(A)
print()
reverseList(A, 0, 5)
print("Reversed list is")
print(A)