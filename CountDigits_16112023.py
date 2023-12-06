def countdigits(num):
    cnt = 0
    while num>0:
        num = int(num/10)
        # print(num)
        cnt+=1
    return cnt


if __name__=='__main__':
    num = int(input("Enter the number: "))
    print(countdigits(num))