# Same logic for smallest element
# This has time complexity of theta(n)
import random
def largestelement(arr):
    if not arr:
        return None
    else:
        num = arr[0]
        for i in range(1,len(arr)):
            if arr[i]>num:
                num=arr[i]
        return num


if __name__=='__main__':
    arr = random.sample(range(10,100),10)
    print(arr)
    print(largestelement(arr))