"""
Loop in link list

Approach =  take two pointers pointing to head (first, second)
speed of second pinter is twice speed of first pointer. (speed(second) = speed(first))

if there is a loop there will be a point where these two will actually meet once. and if the second pointer which is twice the speed of first pointer
comes to NULL or None that means there is no loop.
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
    
    def addLoop(self,index):
        start = end = self.head 
        count = 0
        while (count != index-1):
            start = start.next 
            count += 1
        
        while (end.next != None):
            end = end.next 
        
        end.next = start
    
    def detectLoop(self):
        first = second = self.head 
        while (second.next.next != None):
            first = first.next 
            second = second.next.next
            if (first == second):
                print('Loop present')
                return
        
        if first.next == None or second.next.next == None:
            print("No Loop")
        
        return 
            
        
        
            
        
        

if __name__ == '__main__':
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(85)
    llist.push(25)
    llist.push(31)

    llist.addLoop(3)
    
    llist.detectLoop()
