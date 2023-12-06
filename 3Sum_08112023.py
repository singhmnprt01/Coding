# 3 Sum
# https://leetcode.com/problems/3sum/submissions/

def sum3(mylist):
    myanswerlist=[]
    length = len(mylist)
    # The Most Important Step
    mylist.sort() 
    for i in range(0,len(mylist)):
        if i!=0 and mylist[i]==mylist[i-1]:
            continue;
        j=i+1
        k=length-1
        while j<k:
            sum_= mylist[i]+mylist[j]+mylist[k]
            
            if sum_ ==0:
                myanswerlist.append([mylist[i],mylist[j],mylist[k]])
                # print(sum_)
                # print([mylist[i],mylist[j],mylist[k]])
                j+=1
                k-=1
                while j<k and mylist[j]==mylist[j-1]:
                    j+=1
                while j<k and mylist[k]==mylist[k+1]:
                    k-=1
                
            elif sum_<0:
                j+=1
                
            elif sum_>0:
                k-=1
                
    return myanswerlist
        
        

if __name__ == '__main__':
    mylist = [-1,0,1,2,-1,-4]
    print(sum3(mylist))
    