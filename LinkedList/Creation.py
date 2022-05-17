"""
implementing Link list in python

insertion and deletion complexity of order of O(1)
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        
    def pushLeft(self,data):
        new_node = Node(data)
        
        new_node.next = self.head
        self.head = new_node
        
    def pushRight(self,data):
        new_node = Node(data)
        
        start = self.head
        while (start.next != None):
            start = start.next
        
        start.next = new_node
    
    def push(self,data,index):
        new_node = Node(data)

        if (index == 1):
            new_node.next = self.head
            self.head = new_node
            return
            
        start = self.head    
        count = 0
        while(count != index-2):
            start = start.next
            count +=1
        
        new_node.next = start.next 
        start.next = new_node
        
        return 
    
    def popLeft(self):
        print('popping {}'.format(self.head.data))
        self.head = self.head.next
        
        return
        
    def popRight(self):
        start = self.head 
        while (start.next.next != None):
            start = start.next 
        
        print('popping {}'.format(start.next.data))
        start.next = None
        
        return
    
    def pop(self,index):
        start = self.head 
        if index == 1:
            print('popping {}'.format(self.head.data))
            self.head = self.head.next 
        else:
            count = 0
            while(count != index -2):
                start = start.next 
                count +=1
            
            print('popping {}'.format(start.next.data))
            start.next = start.next.next
            
        return 
        
    def printLinkedlist(self):
        start = self.head
        
        print('elements of link list are :', end = ' ')
        while (start != None):
            print(start.data, end = ' ')
            start = start.next


if __name__ == '__main__':
    ll = Linkedlist()
    ll.pushLeft(3)
    ll.pushLeft(1)
    ll.printLinkedlist()        

    ll.push(2, 2)
    print('')
    ll.printLinkedlist()
    ll.push(0,1)
    ll.pushRight(10)
    ll.pushRight(11)
    print('')
    ll.printLinkedlist()
    print('')
    ll.popLeft()
    print('')
    ll.printLinkedlist()
    print('')
    ll.popRight()
    print('')
    ll.printLinkedlist()
    print('')
    ll.pop(2)
    print('')
    ll.printLinkedlist()
