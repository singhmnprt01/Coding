def sumofdigitsRecursion(num):
    
    # This is called as Base case
    if num<10:
        return num
    
    # or (This will make one more recursion call)
    # if num==0:
    #     return 0 
    
    # These are recursive cases
    return num%10 + sumofdigitsRecursion(num//10)


if __name__=='__main__':
    num = int(input("Enter the number: "))
    print(sumofdigitsRecursion(num))