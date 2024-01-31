class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def add_next(self, data):
       newnode=Node(data)
       self.tail.next=newnode
       self.tail=newnode
    
    # 10 - 20 - 30
    def removeduplicate(self):
        startdata=self.head
        current=self.head.next
        
        while current:
            if startdata.data==current.data:
                startdata.next=current.next
                # delete the node
                current=startdata.next
            else:
                startdata=current
                current=current.next
        return self.head

if __name__=='__main__':
    node1=Node(10)
    ll=LinkedList()
    ll.head=node1
    ll.tail=node1
    ll.add_next(10)
    ll.add_next(20)
    ll.add_next(30)
    # while ll.head:
    #     print(ll.head.data)
    #     ll.head=ll.head.next
    head=ll.removeduplicate()
    while head:
        print(head.data)
        head=head.next