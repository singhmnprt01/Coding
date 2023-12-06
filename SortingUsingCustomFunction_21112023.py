class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        
def myFun(p):
    return p.x;

l = [Point(1,10), Point(10,8), Point(1,5), Point(2,7)]
l.sort(key=myFun)
for i in l:
    print(i.x, "-", i.y)
        