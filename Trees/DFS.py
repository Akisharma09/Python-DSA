"""
Binary Search Tree
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self,data):
        if data == self.data:
            return
        else:
            if data < self.data:
                if self.left:
                    self.left.add_child(data)
                else:
                    self.left = Node(data)
            else:
                if self.right:
                    self.right.add_child(data)
                else:
                    self.right = Node(data)
    
    #left sub tree root right sub tree
    def inorderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.inorderTraversal()
        
        elements.append(self.data)
        
        if self.right:
            elements += self.right.inorderTraversal()
        
        return elements
    
    #root left sub tree right subs tree
    def preorderTraversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.preorderTraversal()
        if self.right:
            elements += self.right.preorderTraversal()
        
        return elements
    
    #left sub tree right sub tree root
    def postorderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.postorderTraversal()
        if self.right:
            elements += self.right.postorderTraversal()
        elements.append(self.data)
        
        return elements
    
        

if __name__ == '__main__':
    root = Node(5)
    root.add_child(10)
    root.add_child(1)
    root.add_child(3)
    root.add_child(16)
    root.add_child(8)
    
    print(root.inorderTraversal())
    
    print(root.preorderTraversal())
    
    print(root.postorderTraversal())
