"""
check if two linked list are intersecting
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.visited_flag = 'N'
        
class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def printLl(self):
        start = self.head
        while(start != None):
            print(start.data)
            start = start.next
    
    def getLength(self):
        start = self.head
        count = 0
        while(start!= None):
            count += 1
            start = start.next
        
        return count
    
def check_intersection(d,max,min):
    head1 = max.head
    head2 = min.head
    while (d!= 0):
        d -=1
        head1 = head1.next
    
    while head1 != None and head2 != None:
        if head1 == head2:
            print('Intersected at {}'.format(head2.data))
            return
        else:
            head1 = head1.next 
            head2 = head2.next
            
    print('No Intersection')
            

if __name__ == '__main__':
    
    ll1 = LinkedList()
    ll1.push(30)
    ll1.push(15)
    ll1.push(9)
    ll1.push(6)
    ll1.push(3)
    
    ll1.printLl()
    
    ll2 = LinkedList()
    ll2.push(10)
    
    ll2.head.next = ll1.head.next.next.next
    
    length_ll1 = ll1.getLength()
    length_ll2 = ll2.getLength()
    
    d = abs(length_ll1 - length_ll2)
    
    if length_ll1 > length_ll2:
        check_intersection(d,ll1,ll2)
    elif length_ll1 == length_ll1:
        print('No Intersection')
    else:
        check_intersection(d,ll2,ll1)       
