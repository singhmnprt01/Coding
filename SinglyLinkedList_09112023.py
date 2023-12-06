# Singly Linked List

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    

class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        current = self.head
        # print(current)
        while current:
            yield current.data
            current = current.next
    
    def __str__(self):
        # print(self)
        return ' --> '.join(str(data) for data in self)
    
    # To insert a node in the beginning
    def push(self,data):
        newnode = Node(data)
        if self.head==None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head = newnode
    
    # To insert a node at last
    def append(self, data):
        newnode = Node(data)
        self.tail.next = newnode
        self.tail = newnode
    
    # To insert a node at a given position
    def insert(self, location, data):
        if location == 0:
            self.push=0
        else:
            newnode = Node(data)
            prevnode = self.head
            index=0
            while index<location-1:
                prevnode = prevnode.next
                index+=1
            nextnode = prevnode.next
            prevnode.next = newnode
            newnode.next=nextnode
            pass;
            
 
if __name__ == '__main__':
    
    node1 = Node(10)
    print(f"node1 is {node1} and data is {node1.data}")
    
    node2 = Node(20)  
    print(f"node2 is {node2} and data is {node2.data}")
    
    # Attaching node 1 and node2 to create a linkedList
    node1.next = node2
    print(f"node1 next is is {node1.next} and data is {node1.next.data}")
    
    # Creating SinglyLinkedList object
    SinglyLinkedList = SinglyLinkedList()
    
    # Attaching Node1 to singlylinkedlist' head
    SinglyLinkedList.head=node1
    
    # Attahcing Noden (here Node2) to singlyLinkedList' tail
    SinglyLinkedList.tail = node2
    
    print(f"SinglyLinkedList is: {SinglyLinkedList}")  
    
    node3 = Node(30)
    node2.next = node3
    SinglyLinkedList.tail = node3
    
    print(f"Updated SinglyLinkedList is: {SinglyLinkedList}")  
    
    SinglyLinkedList.push(0)
    
    print(f"Updated SinglyLinkedList is: {SinglyLinkedList}")
    
    SinglyLinkedList.append(100)
    
    print(f"Updated SinglyLinkedList is: {SinglyLinkedList}")
    
    location = 3
    val = -1
    SinglyLinkedList.insert(location,val)
    
    print(f"Updated SinglyLinkedList after adding {val} at {location} location is: {SinglyLinkedList}")
    
    #  Another way to traverse a LinkedList
    start = SinglyLinkedList.head
    while start:
        print(start.data)
        start=start.next
        # print(start)
    
    # Sort the linkedlist:
    # Method 1: Bubble Sort
    # Method 2: QUick Sort