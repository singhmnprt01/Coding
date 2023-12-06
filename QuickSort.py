import random
def maxsubarray(arr):
    low=0
    high=0
    sum_current=arr[low]
    sum_prev = sum
    while low<high and high<len(arr):
        sum_current=sum_current + arr[high]
        high+=1
        if sum_current<sum_prev:
            sum_current = sum_current - arr[low]
            sum_current = sum_current + arr[high]
            low+=1
            
    return sum_current
        


if __name__ == '__main__':
    arr = random.sample(range(-10,100),10)
    maxsubarray(arr)