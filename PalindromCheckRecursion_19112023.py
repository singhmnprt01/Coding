def palindormcheck(text):
    if len(text)>1:
        if text[0]==text[-1]:
            palindormcheck(text[1:-1])
        else:
            return "False"
    return "True"
        

if __name__ =='__main__':
    text = input("Enter the text: ")
    print(palindormcheck(text))

