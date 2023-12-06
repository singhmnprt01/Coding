# Time Complexity is O(nlogn)
import random
def mergeSort(arr, low, high):
    if high > low:
        # print("Here")
        mid = (low+high)//2
        mergeSort(arr, low, mid)
        mergeSort(arr, mid+1, high)
        merge(arr, low, mid, high)
    return arr

def merge(arr, low, mid, high):
    
    left = arr[low:mid+1]
    right = arr[mid+1:high+1]
    i,j=0,0
    k = low
    
    while i < len(left) and j < len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
            # k+=1
        else:
            arr[k]=right[j]
            j+=1
            # k+=1
        k+=1
        
    while i < len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    while j < len(right):
        arr[k]=right[j]
        j+=1
        k+=1
    # print(arr)


if __name__ == '__main__':
    arr = random.sample(range(1,100),10)
    low=0
    high = len(arr)
    print(arr)
    print(mergeSort(arr, low, high))