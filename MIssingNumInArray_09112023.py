# Code for Missing number in array:
import random
import random

def missingnum(n, arr):
    missing_num=None
    arr.sort() # The most important step. It uses tim sort algo which is a combination of merge and insertion sort
    for i in range(0,len(arr)-1):
        if arr[i+1] - arr[i]>1:
            missing_num = arr[i]+1
            break;
    if missing_num == None:
        if arr[0]==1:
            return n
        else:
            return 1
    else:
        return missing_num
    
def missingnum2(n, arr):
    arr2 = list(set(arr))
    for i in range(1,n+1):
        if i not in arr2:
            return i

if __name__=='__main__':
    n=12
    arr = random.sample(range(1,n+1),n-1)
    print(arr)
    print(set(arr)) # Set sorts the data
    print(missingnum(n, arr))
    print(missingnum2(n, arr))
    
