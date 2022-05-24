"""
Double Linked List
"""

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList():
    def __init__(self):
        self.head = None
    
    def push(self, data):
        #step1
        new_node = Node(data)
        #step2
        new_node.next = self.head
        new_node.prev = None
        #step3
        if self.head is not None:
            self.head.prev = new_node
        #step4
        self.head = new_node
        
    def pushEnd(self,data):
        new_node = Node(data)
        start = self.head
        while start.next is not None:
            start = start.next 
        
        new_node.prev = start
        start.next = new_node
    
    def printDLL(self):
        start = self.head 
        while(start != None):
            print(start.data)
            start = start.next 
    
    def printReverse(self):
        last = self.head 
        while last.next is not None:
            last = last.next 
        
        while(last != self.head):
            print(last.data)
            last = last.prev
        
        print(last.data)
    
    def pushMiddle(self,data,index):
        start = self.head 
        
        while(index -2 != 0):
            start = start.next
        
        new_node = Node(data)
        new_node.next = start.next
        start.next.prev = new_node
        new_node.prev = start
        start.next = new_node
        
        
    def deleteStart(self):
        self.head = self.head.next
    
    def deleteMiddle(self,index):
        middle = self.head 
        while(index-2 != 0):
            middle = middle.next
        
        middle.next.next.prev = middle.next.prev
        middle.next = middle.next.next
    
    def deleteEnd(self):
        end = self.head 
        while (end.next.next is not None):
            end = end.next
        
        end.next = None
     

if __name__ == '__main__':
    dll = DoubleLinkedList()
    dll.push(4)
    dll.push(3)
    dll.push(1)
    
    dll.printDLL()
    
    dll.pushMiddle(2,2)
    print('Pushing 2 in at index 2.')
    dll.printDLL()
        
    dll.pushEnd(5)
    print('Pushing 5 in at index 5.')
    dll.printDLL()    
    
    
    print('deleting element from start.')
    dll.deleteStart()
    
    print('Printing List:')
    dll.printDLL()     

    print('Printing in reverse')
    dll.printReverse()      
    
    print('deleting element at position 2 i.e. 3')
    dll.deleteMiddle(2)
    
    print('Printing List:')
    dll.printDLL()
    
    print('deleting last element i.e. 5')
    dll.deleteEnd()
    
    print('Printing List:')
    dll.printDLL()
