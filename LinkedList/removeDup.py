"""
Remove duplicate in unsorted linked list

Approach is use hash/set 
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
        
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def printLinkedList(self):
        start = self.head 
        while(start.next is not None):
            print(start.data)
            start = start.next 
        print(start.data)
    
    def deleteDup(self):
        hash_ = set()
        start = self.head
        
        hash_.add(start.data)
        while(start.next is not None):
            if start.next.data in hash_:
                start.next = start.next.next
            else:
                hash_.add(start.next.data)
                start = start.next
        
        if start.data in hash_:
            start = None
        
    
if __name__ == '__main__':
    ll = linkedList()
    ll.push(11)
    ll.push(12)
    ll.push(13)
    ll.push(11)
    ll.push(13)
    ll.push(14)
    
    print('Deleting duplicate')
    ll.deleteDup()
    
    ll.printLinkedList()
