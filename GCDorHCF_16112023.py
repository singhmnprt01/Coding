def gcd(num1,num2):
    start =int((min(num1,num2))/2)
    mygcd=1
    for i in range(start,num1+1):
        if num1%i==0 and num2%i==0:
            mygcd = i
    return mygcd
    # pass;


if __name__=='__main__':
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the 2nd number: "))
    print(gcd(num1,num2))