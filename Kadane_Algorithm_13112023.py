import random
def maxsubarray(arr):
    sum_c, sum_p = arr[0], arr[0]
    # Approach 1
    for i in range(1,len(arr)):
         sum_c = max(sum_c+arr[i],arr[i])
         sum_p = max(sum_p, sum_c)
    return sum_p


if __name__ == '__main__':
    arr = random.sample(range(-10,10),5)
    print(arr)
    print(maxsubarray(arr))