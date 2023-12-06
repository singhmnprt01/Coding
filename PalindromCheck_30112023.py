def palcheck(s1):
    l=0
    r=len(s1)-1
    checker=0
    while l<r:
        if s1[l]!=s1[r]:
            checker=1;
            # print(checker)
            break;
        l+=1
        r-=1
    
    if checker==0:
        return True
    else:
        return False

if __name__=='__main__':
    s1='sabcbas'
    print(s1)
    print(palcheck(s1))