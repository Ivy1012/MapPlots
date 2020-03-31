def rightRotate(arr, d, n):
    for i in range(d):
        rightRotatebyOne(arr, n)
    return arr
def rightRotatebyOne(arr, n):
    temp = arr[n-1]
    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = temp