def reverseTheString_method1(mystr):
    helper=[]
    wrd = ""
    for i in range(0,len(mystr)+1):
        
        if i==len(mystr) or mystr[i]==" ":
            helper.append(wrd)
            wrd = ""    
        else:
            wrd +=mystr[i]
            
    mystr2=""
    for i in range(len(helper)-1,-1,-1):
       print(helper[i]," ")
    # return mystr2

if __name__=='__main__':
    mystr = input("Enter the string: ")
    reverseTheString_method1(mystr)