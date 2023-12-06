def lcm(num1, num2):
    start = max(num1,num2)
    cnt =0
    while cnt!=1:
        if start%num1==0 and start%num2==0:
            cnt+=1
            break;
        start+=1
        
    return start



if __name__=='__main__':
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the 2nd number: "))
    print(lcm(num1,num2))