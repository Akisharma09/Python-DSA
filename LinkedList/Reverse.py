"""
Reversing a linked list
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def reverse(self):
        prev = None
        current = self.head
        
        while (current != None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        self.head = prev
    
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node 
    
    def printLinkedlist(self):
        start = self.head
        while start != None:
            print(start.data)
            start = start.next
    


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(85)
    
    llist.printLinkedlist()
    
    llist.reverse()
    print('printing in reverse')
    llist.printLinkedlist()    
