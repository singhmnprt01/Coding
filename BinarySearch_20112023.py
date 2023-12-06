# It's time complexity for successful search O(logn) and for unsuccessful search Theta(logn)
# For more details: https://practice.geeksforgeeks.org/batch/ds-with-python/track/searching-basic-python/video/MjExMg%3D%3D


import random
def binarysearch(myarr,num):
    middle = int(len(myarr)/2)
    # print(myarr[middle])
    
    if len(myarr)>1:
        if num<myarr[middle]:
            # print(myarr[0:middle])
            return binarysearch(myarr[0:middle], num)
        elif num>myarr[middle]:
            # print(myarr[middle+1:])
            return binarysearch(myarr[middle+1:], num)
        else:
            # print("Number found")
            return True
    else:
        # print("Size of array is 2")
        # print(myarr)
        if num==myarr[0] :
            # print("Number found")
            return True
        else:
            # print("Number not found")
            return False
        
if __name__=='__main__':
    arr = random.sample(range(1,1000),15)
    arr.sort()
    print(arr)
    num = int(input("Enter the number to be searched: "))
    if binarysearch(arr,num):
        print("Number found")
    else:
        print("Number not found")