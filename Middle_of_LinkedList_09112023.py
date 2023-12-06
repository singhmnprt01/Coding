class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    def __str__(self):
        return ' --> '.join(str(data) for data in self)
    
    def append(self,data):
        newnode = Node(data)
        self.tail.next = newnode
        self.tail = newnode
        
    
if __name__=='__main__':
      
    node1 = Node(10)
    
    SinglyLinkedList = SinglyLinkedList()
    SinglyLinkedList.head = node1
    SinglyLinkedList.tail=node1
    
    SinglyLinkedList.append(20)
    SinglyLinkedList.append(30)
    SinglyLinkedList.append(40)
    SinglyLinkedList.append(50)
    SinglyLinkedList.append(90)
    
    print(SinglyLinkedList)
    
    # Let's fine the middle element:
    p1 = SinglyLinkedList.head
    p2=SinglyLinkedList.head
    
    while p2 and p2.next:
        p2 = p2.next.next
        p1 = p1.next
    print(f"Middle element is: {p1.data}")
    
  
        