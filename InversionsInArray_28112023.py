# Time complexity is theta(nlogn)

import random
def countInversions(arr, l, r):
    res = 0
    if l<r:
        m = (l+r)//2
        res+= countInversions(arr, l, m)
        res+= countInversions(arr, m+1,r)
        res+= countMerge(arr, l, m, r)
    
    return res;

# This is more or less standard merge sort function
def countMerge(arr, l, m , r):
    left = arr[l:m+1]
    right = arr[m+1:r+1]
    res, i, j, k =0,0,0,l
    
    while i < len(left) and j < len(right):
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
            res += len(left) -i #an extra step
        k+=1
    
    while i< len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    
    while j < len(right):
        arr[k]=right[j]
        j+=1
        k+=1
    
    return res

if __name__ =='__main__':
    arr = random.sample(range(1,20),10)
    print(arr)
    l = 0
    r = len(arr)-1
    countInversions(arr)