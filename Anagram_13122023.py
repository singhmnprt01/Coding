def anagram(s1,s2):
    mycount= [0]*256
    
    if len (s1)!=len(s2):
        return False
    else:
        for i in range(0,len(s1)):
            mycount[ord(s1[i])]+=1
            mycount[ord(s2[i])]-=1
    
    for x in mycount:
        if x!=0:
            return False
    return True


if __name__=='__main__':
    s1 = input("Enter the frist string: ")
    s2 = input("Enter the second string: ")
    print(anagram(s1,s2))    