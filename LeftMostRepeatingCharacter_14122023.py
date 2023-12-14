
import sys
def leftmost_method1(mystr):
    
    helper = [0]*256
    
    for i in range(0,len(mystr)):
        helper[ord(mystr[i])]+=1
    
    for i in range(len(mystr)):
        if helper[ord(mystr[i])] >1:
            return i
    return -1

def leftmost_method2(mystr):
    helper = [-1]*256
    result = sys.maxsize
    for i in range(len(mystr)):
        ord_value =  ord(mystr[i])
        
        if helper[ord_value]==-1:
            helper[ord_value]=i
            
        else:
            result = min(result, helper[ord_value])
    
    if result == sys.maxsize:
        return -1
    else:
        return result

        
if __name__ == '__main__':
    mystr = input("Enter the stirng: ")
    print(leftmost_method1(mystr))
    print(leftmost_method2(mystr))