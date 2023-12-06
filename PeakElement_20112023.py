def peakelement(arr, low, high):
    mid = (low +high)//2
    print(low,"-", mid, "-", high)
    
    if mid == high:
        return 1
    
    elif arr[mid] > arr[mid-1] and arr[mid]<arr[mid+1]:
        print("Running this")
        return peakelement(arr, mid+1, high)
    
    elif arr[mid] < arr[mid-1] and arr[mid] > arr[mid+1]:
        return peakelement(arr, low, mid-1)
    
    elif arr[mid]> arr[mid-1] and arr[mid]> arr[mid+1]:
        return 1
    
    else:
        return 0

if __name__=='__main__':
    # arr = [1,2,3,4,5,6,7,8]
    # arr=[1,2,3]
    # arr=[5,4,3,2,1]
    low=0
    high=len(arr)-1
    print(peakelement(arr, low, high))
    