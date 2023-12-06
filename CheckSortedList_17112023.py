import random
def checksortedlist(arr):
    if not arr:
        return "Yes"
    elif len(arr)==1:
        return "Yes"
    else:
        increasing, decreasing = 0,0
        myreturn = "Yes"
        for i in range(len(arr)-1):
            if arr[i+1]>arr[i]:
                increasing+=1
            elif arr[i+1]<arr[i]:
                decreasing+=1
            
            if increasing >0 and decreasing>0:
                myreturn="No"
                break;
        return myreturn
        


if __name__=='__main__':
    arr = random.sample(range(10,100),10)
    # arr=[]
    print(arr)
    print(checksortedlist(arr))