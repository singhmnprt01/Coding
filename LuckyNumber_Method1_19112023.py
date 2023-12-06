# The method is slightly lenghty but works well 

def isdelete(myarr, ite):
    # if len(myarr)>=ite:
        for i in range(ite-1,len(myarr), ite):
            myarr[i]=-1
        temp=[]
        for i in range(0,len(myarr)):
            if myarr[i]>0:
                temp.append(myarr[i]) 
        # print(temp) 
        return temp

def luckynumber(myarr,num,ite):
    
    if len(myarr)>=ite:
        temp = isdelete(myarr=myarr, ite=ite)
        if len(temp)>0:
            ite+=1
            return luckynumber(myarr=temp,num=num, ite=ite)
    else:
            if myarr[-1]==num:
                # print(myarr[-1])
                return (f"{myarr[-1]} is a lucky Number")
            else:
                return (f"{num} is not lucky Number")
                

if __name__=='__main__':
    num = int(input("Enter the number: "))
    myarr = []
    [myarr.append(i) for i in range(1,num+1)]
    # print(myarr)
    ite=2
    print(luckynumber(myarr,num, ite=ite))