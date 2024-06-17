from collections import Counter
def anagram1(s1,s2):
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


def anagram2(s, t):
        mydict = {}
        if len(s)!=len(t):
            return False
        z=0    
        for i in s:
            mydict.setdefault(i, 0)
            mydict[i]-=1
        
        for j in t:
            try:
                mydict[j] = mydict[j]+1
            except:
                z=1
                break;
        if z==0:
            for i in mydict.values():
                if i!=0:
                    return False
            return True
        else:
            return False

def anagram3(s,t):
    s1 = Counter(s)
    t1 = Counter(t)
    return s1==t1

if __name__=='__main__':
    s1 = input("Enter the frist string: ")
    s2 = input("Enter the second string: ")
    print(anagram1(s1,s2))    
    print(anagram2(s1,s2))  
    print(anagram3(s1,s2)) 