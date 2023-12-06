def factorecur(num):
        if num<=0:
            return 1
        else:
            return num*factorecur(num-1)
            
if __name__=='__main__':
    num = int(input("Enter the number: "))
    print(factorecur(num))