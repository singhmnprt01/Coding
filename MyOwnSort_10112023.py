import random
def mysort(myarr):
    low = 0
    high = len(myarr)    
    for i in range(low, len(myarr)):
        for j in range(low,high):
            if myarr[high-1]<myarr[j]:
                temp = myarr[j]
                myarr[j]=myarr[high-1]
                myarr[high-1]= temp
        high-=1
    return myarr


if __name__ == '__main__':
    myarr = random.sample(range(1,100),10)
    print(f" Before sorting: {myarr}")
    print(f"Afer soring: {mysort(myarr)}")