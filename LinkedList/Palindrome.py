"""
check palindrome in single link list

Approach:
push all elements in stack 

Then pop element from stack and check it with elements in Linked list. If the elements didn't match return and print not Palindrome.
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList():
    def __init__(self):
        self.head = None


    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def printLinkedList(self):
        start = self.head
        while (start.next != None):
            print(start.data)
            start = start.next 
    
    def checkPalindrome(self):
        stack = []
        start = self.head 
        while (start != None):
            stack.append(start.data)
            start = start.next 
            
        stack = stack[::-1]
        i = 0
        start = self.head
        
        while(start != None):
            if (start.data != stack[i]):
                print('Not palindrome')
                return
            i +=1
            start = start.next
            
            
        print('palindrome')

if __name__ == '__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(3)
    llist.push(2)
    llist.push(1)                
               
    llist.checkPalindrome()         
