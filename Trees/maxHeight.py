class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_node(self, data):
        new_node = Node(data)
        if data < self.data:
            if self.left is not None:
                self.left.add_node(data)
            else:
                self.left = new_node
        else:
            if self.right is not None:
                self.right.add_node(data)
            else:
                self.right = new_node

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data, end=" ")
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data, end=" ")

    def preorder(self):
        print(self.data, end=" ")
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()

    def height_of_tree(self):
        left_height, right_height = -1, -1
        if self is None:
            return -1
        if self.left:
            left_height = self.left.height_of_tree()
        if self.right:
            right_height = self.right.height_of_tree()

        return max(left_height, right_height)+1


if __name__ == '__main__':
    root = Node(5)
    root.add_node(2)
    root.add_node(10)
    root.add_node(7)
    root.add_node(15)
    root.add_node(12)
    root.add_node(20)
    root.add_node(30)
    root.add_node(6)
    root.add_node(8)

    root.inorder()
    print("", end="\n")
    root.postorder()
    print("", end="\n")
    root.preorder()
    print("", end="\n")
    print(root.height_of_tree())
