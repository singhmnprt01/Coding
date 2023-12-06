import random

def insertionsort(arr):
    low = 0
    high = len(arr)
    
    for i in range(1,len(arr)):
        numb = arr[i]
        j=i-1
        while j>=0 and numb < arr[j]:
            arr[j+1]=arr[j]
            arr[j]=numb
            j-=1
    return arr
         
                
if __name__ == '__main__':
    myarr = random.sample(range(1,100),12)
    print(myarr)
    print(insertionsort(myarr))
