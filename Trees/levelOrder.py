def levelOrder(root):
    #Write your code here
    q = [root]
    while len(q) != 0:
        temp = q.pop(0)
        print(temp.info, end = " ")
        if temp.left is not None:
            q.append(temp.left)
        if temp.right is not None:
            q.append(temp.right)
