def longplaindrome(mystr):
    if len(mystr)<=1:
        return mystr;
    result=""
    resultLen=0
    for i in range(1,len(mystr)):
        # odd length palindromes
        low, high= i,i
        # high = i
        while low >= 0 and high < len(mystr):
            if mystr[low]!=mystr[high]:
                break;
            else:
                if high-low+1> resultLen:
                    result=mystr[low:high+1]
                    resultLen=len(result)
                low-=1
                high+=1
                
        # even length palindrome
        low, high = i, i+1
        while low >= 0 and high < len(mystr):
            if mystr[low]!=mystr[high]:
                break;
            else:
                if high-low+1> resultLen:
                    result=mystr[low:high+1]
                    resultLen=len(result)
                low-=1
                high+=1          
    return result
                
if __name__=='__main__':
    mystr = "bacddcabsa"
    print(mystr[0:])
    print(longplaindrome(mystr=mystr))