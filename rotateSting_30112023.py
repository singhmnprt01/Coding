# Source: https://practice.geeksforgeeks.org/batch/ds-with-python/track/string-basic-python/video/Mzk0Mg%3D%3D
def rotateString(s1,s2):
    if len(s1)!=len(s2):
        return False
    else:
        temp = s1+s1
        if temp.find(s2)!= -1:
            return True
        else:
            return False


if __name__=='__main__':
    s1="ABCD"
    s2="CDAB"
    print(rotateString(s1,s2))