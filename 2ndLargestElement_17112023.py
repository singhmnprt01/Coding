import random
def secondlargest(arr):
    highest = arr[0]
    second = None
    for i in range(1,len(arr)):
        if arr[i]>highest:
            second = highest
            highest = arr[i]

        elif arr[i]!=highest:
            if second==None or second < arr[i]:
                second = arr[i]
    return second
    # pass;



if __name__=='__main__':
    arr = random.sample(range(10,100),12)
    # arr=[83, 60, 14, 27, 77, 41, 61, 54, 82, 21, 45, 31]
    print(arr)
    print(secondlargest(arr))