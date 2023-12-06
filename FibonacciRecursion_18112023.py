# Print the nth fibonacci number
def fib_recur(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fib_recur(num-1) + fib_recur(num-2)


if __name__=='__main__':
    num = int(input("Enter the number: "))
    print(fib_recur(num))