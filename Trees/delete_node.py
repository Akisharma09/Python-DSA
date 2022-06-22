"""
Binary Search Tree
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
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

    # left sub tree root right sub tree
    def inorderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.inorderTraversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inorderTraversal()

        return elements

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

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min_val = self.right.findMin()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self


if __name__ == '__main__':
    root = Node(5)
    root.add_child(10)
    root.add_child(1)
    root.add_child(3)
    root.add_child(16)
    root.add_child(8)

    print(root.inorderTraversal())
    root.delete(3)
    print(root.inorderTraversal())
