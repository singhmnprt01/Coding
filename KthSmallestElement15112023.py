import random
def kthSmallesElement(arr,k):
    # Approach 1: Sort the array using python's inbuild sort and return value arr[k]
    
    # Approach 2: Create a sorting function like bubble sort and then find the element
    
    # InsertionSort:
    for i in range(1,len(arr)):
        temp1=arr[i]
        j=i-1
        while j>=0 and arr[j]>temp1:
            # print(arr[j+1], " ", temp1 )
            temp2 = arr[j+1]
            # Actually this arr[j+1] is same as temp1 as the list is getting sorted, temp1 is same as arr[j+1]
            # Temp1 is moving towards left to get thr right position hence arr[j+1] is always same as temp1
            
            arr[j+1] = arr[j]
            arr[j]=temp2
            j-=1
            
    print(arr)
    return arr[k-1]


if __name__ == '__main__':
    arr = random.sample(range(1,100),10)
    print(f"Initial Array: {arr}")
    k=4
    print(f"{k} smallest element is {kthSmallesElement(arr,k)}")
    