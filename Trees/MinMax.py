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
    
    def findMin(self):
        if self.left is None:
            return self.data
        else:
            return self.left.findMin()
    
    def findMax(self):
        if self.right:
            return self.right.findMax()
        else:
            return self.data

if __name__ == '__main__':
    root = Node(5)
    root.add_child(10)
    root.add_child(1)
    root.add_child(3)
    root.add_child(16)
    root.add_child(8)
    
    print(root.findMin())
    print(root.findMax())
