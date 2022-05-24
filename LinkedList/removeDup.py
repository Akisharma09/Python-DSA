"""
Remove duplicate in unsorted linked list
Approach: Use hash/set 

Remove duplicate from sorted
Approach: if current.data == current.next.data then current.next = current.next.next else current = current.next

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
    
    def deleteDupUnsorted(self):
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
    
    def removeDupSorted(self):
        start = self.head 
        while(start.next is not None):
            if start.data == start.next.data:
                if start.next.next is not None:
                    start.next = start.next.next
                else:
                    start.next = None
            else:
                start = start.next 
        
    
if __name__ == '__main__':
    ll = linkedList()
    ll.push(11)
    ll.push(12)
    ll.push(13)
    ll.push(11)
    ll.push(13)
    ll.push(14)
    
    print('Deleting duplicate')
    ll.deleteDupUnsorted()
    
    ll.printLinkedList()
    
    l2 = linkedList()

    l2.push(4)
    l2.push(4)
    l2.push(3)
    l2.push(2)
    l2.push(2)
    l2.push(1)
    l2.removeDupSorted()
    
    print('Deleting duplicate')
    ll.deleteDupUnsorted()
    
    l2.printLinkedList()
    
