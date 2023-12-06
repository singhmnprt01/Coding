import random
# from .LomutoPartition_30112023 import lomutoPartition
def quicksort(arr, l, h):
    if l < h:
        p = lomutoPartition(arr, l, h)
        quicksort(arr,l, p-1)
        quicksort(arr, p+1,h)
    return arr

def lomutoPartition(arr, l, h):
    pivot = arr[h]
    i=l-1
    for j in range(l,h):
        if arr[j]<pivot:
            i+=1
            arr[j], arr[i]=arr[i], arr[j]
    arr[i+1], arr[h]= arr[h], arr[i+1]
    return arr.index(pivot)
    


if __name__=='__main__':
    arr = random.sample(range(1,100),10)
    print(arr)
    l=0
    h = len(arr)-1
    print(quicksort(arr, l, h))
    
    