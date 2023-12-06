import math
def alldivisors(num):
    high = int(math.sqrt(num))
    div_list=[]
    for i in range(2,high+1):
        if num%i==0:
            div_list.append(i)
            div_list.append(int(num/i))
    return div_list



if __name__=='__main__':
    num=int(input("Enter the number: "))
    print(alldivisors(num))