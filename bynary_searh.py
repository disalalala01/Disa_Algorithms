A = [1,12,45,65,86,91,92,100,111]
start = 0
stop = len(A)
key = 45
a = 55

def binary_search(A:list, key:int, start:int, stop:int):
    if start > stop:
        return False
    middle = (start+stop)//2
    if key == A[middle]:
        return middle
    elif key < A[middle]:
         return binary_search(A, key, start, middle-1)
    else:
        return binary_search(A, key, middle+1, stop)

s = binary_search(A, a, start , stop)

print(s)
