def leftmost(mystr):
    
    helper = [0]*256
    
    for i in range(0,len(mystr)):
        helper[ord(mystr[i])]+=1
    
    for i in range(len(mystr)):
        if helper[ord(mystr[i])] >1:
            return i
    return -1
        
if __name__ == '__main__':
    mystr = input("Enter the stirng: ")
    print(leftmost(mystr))