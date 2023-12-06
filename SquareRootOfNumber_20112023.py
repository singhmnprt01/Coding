# Question - Find square root of a number

def squareRoot(num, low, high):
    
    if low*low > num:
        high = low
        low = low//2
        return squareRoot(num, low, high)
    elif low*low<num:
        while low*low<=num:
            low+=1
        return low-1
                
        


if __name__=='__main__':
    num = int(input("Enter the number: "))
    
    print(squareRoot(num,num//2, num))