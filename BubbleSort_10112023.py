import random
def bubblesort(myarr):
    low = 0
    high = len(myarr)    
    for i in range(len(myarr)):
        swap=False
        for j in range(low,high-i-1):
            if myarr[j]>myarr[j+1]:
                myarr[j], myarr[j+1]= myarr[j+1], myarr[j]
                swap=True
        if swap==False:
            break;
        # high-=1
    return myarr


if __name__ == '__main__':
    myarr = random.sample(range(1,100),10)
    print(f" Before sorting: {myarr}")
    print(f"Afer soring: {bubblesort(myarr)}")