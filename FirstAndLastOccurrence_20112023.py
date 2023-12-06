import random
import math
def FirstOccurence(arr, low, high, num):
    if low>high:
        return -1
    
    mid = math.floor((low + high)//2)
    
    if num > arr[mid]:
        # print("Num > arr[mid]")
        return FirstOccurence(arr, mid+1, high, num)
    elif num < arr[mid]:
        # print("Num < arr[mid]")
        return FirstOccurence(arr, low, mid-1, num)
    
    else:
        # To find the first occurence
        if mid ==0 or arr[mid-1]!=arr[mid]:
                return mid
        
        else:
        #    print(low, " ", mid, " ", high)
           return FirstOccurence(arr, low, mid-1, num )

def LastOccurence(arr, low, high, num):
    if low>high:
        return -1
    
    mid = math.floor((low + high)//2)
    
    if num > arr[mid]:
        # print("Num > arr[mid]")
        return LastOccurence(arr, mid+1, high, num)
    elif num < arr[mid]:
        # print("Num < arr[mid]")
        return LastOccurence(arr, low, mid-1, num)
    
    else: 
        # To find the last occurence 
        if mid==len(arr)-1 or arr[mid+1]!=arr[mid]:
            return mid
        else:
        #    print(low, " ", mid, " ", high)
           return LastOccurence(arr, mid+1, high, num )


if __name__=='__main__':
    # myarr = random.sample(range(1,10),9)
    myarr=  [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
    myarr.sort()
    print(f"Sorted array is:{myarr}")
    num = int(input("Enter the num to get its first and kast occurence: "))
    low=0
    high = len(myarr)-1
    # print(high)
    first = FirstOccurence(arr=myarr, low=low, high=high, num=num)
    last = LastOccurence(arr=myarr, low=low, high=high, num=num)
    print(first, ",", last)