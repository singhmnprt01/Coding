# Using Bubble Sort

import random

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        newnode = Node(data)
        self.tail.next = newnode
        self.tail = newnode
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    def __str__(self):
        return '-->'.join(str(data) for data in self)

    def sortlinkedlist(self):
            # start = SinglyLinkedList.head
        end = self.tail
        tailsetter = True
        while end!=self.head:
            swap= False
            start_copy = self.head
            while start_copy.next!=end:
                if start_copy.data > start_copy.next.data:
                    start_copy.data, start_copy.next.data = start_copy.next.data, start_copy.data
                    swap=True
                start_copy=start_copy.next
            if tailsetter:
                self.tail = start_copy
                tailsetter=False
            if swap==False:
                break;
            end = start_copy
        # print(SinglyLinkedList)
        # return SinglyLinkedList
        
        
            
    pass;

if __name__ == '__main__':
    node1 = Node(random.randint(1,100))
    SinglyLinkedList = SinglyLinkedList()
    
    SinglyLinkedList.head = node1
    SinglyLinkedList.tail = node1
    
    myarr = random.sample(range(1,100),9)
    for num in myarr:
        SinglyLinkedList.append(num)
    
    print(SinglyLinkedList)
    print(SinglyLinkedList.head.data)
    print(SinglyLinkedList.tail.data)
    print(SinglyLinkedList.sortlinkedlist())
    print(SinglyLinkedList)
        
        
        