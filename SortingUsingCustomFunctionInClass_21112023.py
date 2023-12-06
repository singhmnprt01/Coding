# Source: https://practice.geeksforgeeks.org/batch/ds-with-python/track/sorting-basic-python/video/MjExNQ%3D%3D

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __lt__(self, other):
        return self.x < other.x
    
l = [Point(1,2), Point(10,10), Point(3,3)]
l.sort()
for  i in l:
    print(i.x,"-", i.y)


# Here's a simplified view of how the sorting process might look:

# 1. Compare `Point(1,2)` and `Point(10,10)`. Since `1 < 10`, `Point(1,2)` is considered smaller.
# 2. Compare `Point(1,2)` and `Point(3,3)`. Since `1 < 3`, `Point(1,2)` is still considered smaller.
# 3. Compare `Point(10,10)` and `Point(3,3)`. Since `3 < 10`, `Point(3,3)` is considered smaller.

# So the sorted list is `[Point(1,2), Point(3,3), Point(10,10)]`.