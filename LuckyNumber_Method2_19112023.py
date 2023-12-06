def isLucky(num, counter):
    if num <=counter:
        return True
    
    #  Initially the num is at num position:
    # example 7 is at 7th position from 1 to 7
    
    while num >= counter:
        
        if num % counter ==0:
            return False
    
        # Now here, in the first loop when counter==2,  the position of 7th has changed from 7th to 4th 
        # How? 1,2,3,4,5,6,7 -> 7 at 7th position
        # now when we delete every 2nd element, the position of 7 is :
        # 1,3,5,7 -> at 4th position  
        # So, position = 7 - 7//2
        num = num - num // counter
        counter +=1
    return True
        


if __name__=='__main__':
    num = int(input("Enter the number:"))
    print(isLucky(num=num, counter=2))