# Approach 1: Recursion: Time complexity is Theta(logn)
def computingpower(x,n):
    if n==0:
        return 1
    temp = computingpower(x,int(n/2))
    temp=temp*temp
    
    if n%2==0:
        return temp 
    else:
        return temp*x

# Approach 2: Simple For loop: Time complexity is Theta(n)



if __name__ == '__main__':
    x = int(input("Enter the number: "))
    n = int(input("Enter the power: "))
    print(computingpower(x,n))