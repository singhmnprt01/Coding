
# Time complexity is Theta(n^2) in all cases
# Good thing is that it does less memory writes compared to quick, merge, insertion, etc. sorts
# Heap sort idea is based on selection sort
# It's not a stable sort
# it's an in place algo i.e doesn't require extra space for sorting

import random

def selectionSort(arr):
    low = 0 
    high = len(arr)-1
    
    for i in range(low, high):
        j = i+1
        min_ind = i
        # The below loop is to find the minimum element from i+1 to high and replace it with i.
        # So that, we have minimum element moving to the left
        while j < high:
            if arr[j] < arr[min_ind]:
                min_ind=j
            j+=1
        arr[min_ind], arr[i] = arr[i], arr[min_ind]  
              
    return arr

if __name__ =='__main__':
    arr = random.sample(range(1,100),10)
    print(arr)
    print(selectionSort(arr))