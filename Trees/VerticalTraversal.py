def findMinMax(node, minimum, maximum, hd):
        if node is None:
            return
        elif hd < minimum[0]:
            minimum[0] = hd
        elif hd > maximum[0]:
            maximum[0] = hd
        
        findMinMax(node.left,minimum,maximum,hd-1)
        findMinMax(node.right,minimum,maximum,hd+1)

def printVertical(node,line_no,hd, ret_list):
    if node is None:
        return
    
    if hd == line_no:
        ret_list.append(node.data)
        
    printVertical(node.left,line_no,hd-1, ret_list)
    printVertical(node.right,line_no,hd+1, ret_list)
        
class Solution:
    
    #Function to find the vertical order traversal of Binary Tree.
    def verticalOrder(self, root): 
        #Your code here
        minimum = [0]
        maximum = [0]
        ret_list = []
        findMinMax(root,minimum, maximum, 0)
        for line_no in range(minimum[0], maximum[0]+1):
            printVertical(root,line_no,0, ret_list)
        
    
        return ret_list
