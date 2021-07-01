#  practice
def iterative(arr, n):
    low = 0
    high = len (arr)-1
    mid  = 0
    while low <= high:
        mid = (low + high)//2
        if arr[mid] < n:
            low = mid + 1
        elif arr [mid] > n:
            high = mid - 1
        else:
            return mid

    return -1

arr = [1,2,3,4,5,7,8,9,10]
n = 8

rslt = iterative(arr, n)
if rslt != -1:
    print('index:', rslt)
else:
    print('not present') 