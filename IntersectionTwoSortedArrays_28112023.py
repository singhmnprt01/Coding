def intersection(arr1, arr2):
    i,j=0,0
    
    while i < len(arr1) and j < len(arr2):
        if i>0 and arr1[i-1]==arr1[i]:
            i+=1
            continue;
        
        if arr1[i]>arr2[j]:
            j+=1
        
        elif arr2[j]>arr1[i]:
            i+=1
            
        elif arr1[i]==arr2[j]:
            i+=1
            j+=1
            print(arr1[i])


if __name__=='__main__':
    arr1 = [3,5,5,10,10,15,15,20]
    arr2=[5,10,10,15,30]
    intersection(arr1, arr2)