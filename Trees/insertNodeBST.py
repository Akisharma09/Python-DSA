# Approach1
def insertion(self,node,val):
        if node is None:
            node = Node(val)
        elif val < node.info:
            node.left = self.insertion(node.left,val)
        elif val > node.info:
            node.right = self.insertion(node.right,val)    
        return node
    
    def insert(self, val):
        #Enter you code here.
        if self.root is None:
            self.root = Node(val)
        else:
            self.insertion(self.root,val) 

            
#Approach 2:
def insert(self, val):
        #Enter you code here.
        if self.root is None:
            self.root =  Node(val)
            return self.root
        else:
            curr = self.root
            while True:
                if val < curr.info:
                    if curr.left is not None:
                        curr = curr.left
                    else:
                        curr.left = Node(val)
                        break
                elif val > curr.info:
                    if curr.right is not None:
                        curr = curr.right
                    else:
                        curr.right = Node(val)
                        break
        return self.root
