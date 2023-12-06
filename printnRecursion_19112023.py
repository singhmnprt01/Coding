def print1ton(num):
    if num<=0:
        return
    print1ton(num-1)
    print(num)
    
def printnto1(num):
    if num<=0:
        return
    print(num)
    printnto1(num-1)
    

if __name__=='__main__':
    num = int(input("Enter the number: "))
    print(print1ton(num))
    print(printnto1(num))
    