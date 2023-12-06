import random

def predthecol(arr):
    counter=0
    numzerotracker=[]
    for col in range(0,cols):
        for row in range(0,rows):
            if arr[row][col]==0:
                counter+=1
        numzerotracker.append(counter)
        counter=0
    if max(numzerotracker) ==0:
            return -1
    else:    
            return numzerotracker.index(max(numzerotracker))


if __name__ == '__main__':
    # create a 2D array with 3 rows and 4 columns
    rows = cols =  3
    # arr = [[random.randint(0, 9) for j in range(cols)] for i in range(rows)]
    arr = [[0,0,0],
           [1,0,0],
           [1,0,0]]
    print(arr)
    print(predthecol(arr))