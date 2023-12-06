# arr1 is on the left side of arr2

def mergeSortedArrays(arr1, arr2):
    i,j=0,0
    mergedArray=[]
    while i <len(arr1) and  j < len(arr2):
        if arr1[i]<=arr2[j]:
            print(f"i = {i}")
            mergedArray.append(arr1[i])
            i+=1
        elif arr2[j]<arr1[i]:
            print(f"j = {j}")
            mergedArray.append(arr2[j])
            j+=1
    while i < len(arr1):
        mergedArray.append(arr1[i])
        i+=1
    
    while j < len(arr2):
        mergedArray.append(arr2[j])
        j+=1
    return mergedArray
            


if __name__ == '__main__':
    arr1=[10,15]
    arr2=[5,6,6,30,40]
    print(mergeSortedArrays(arr1=arr1, arr2=arr2))
    