import random
def lomutoPartition(arr, l, h):
    pivot = arr[h]
    i = l-1
    for j in range(l,h):
        if arr[j]<pivot:
            i+=1
            arr[i], arr[j]=arr[j], arr[i]
    arr[i+1], arr[h]=arr[h], arr[i+1]
    return arr


if __name__=='__main__':
    arr = random.sample(range(1,100),10)
    l=0
    h = len(arr)-1
    print(arr)
    print(lomutoPartition(arr, l, h))