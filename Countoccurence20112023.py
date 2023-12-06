
# Method1: Find FirsOccurence and LastOccurence and do: LastOccurence - FirstOccurence + 1
# This Method 1 is more efficient as its time complexity is O(logn)
# Whereas method 2 has time complexity of O(logn + k)

# method 2:
def countoccurence(arr, low, high, num):
    mid = (low+high) //2

    if num < arr[mid]:
        return countoccurence(arr, low, mid-1, num)
    elif num> arr[mid]:
        return countoccurence(arr, mid+1, high,num)
    else:
        count=0;
        for i in range(low, high+1):
            if arr[i]==num:
                count+=1
        return count;


if __name__=='__main__':
    arr = [10,20,20,20,20,30,30,40,50,60,70,70]
    num = 70
    low = 0
    high = len(arr)-1
    print(countoccurence(arr, low, high, num))