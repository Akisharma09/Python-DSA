"""
Max heap using list
self.heap = [0] 
parent = i/2
left = i*2
right = i*2 +1

heap user method
public: push pop peek

heap private method: __bubbleDown, __floatUp, __swap

"""

class maxHeap:
    def __init__(self,items):
        super().__init__()
        self.heap = [0]
        
        for i in items:
            self.heap.append(i)
            self.__floatUp(len(self.heap)-1)
            
    
    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            False
    
    def push(self,item):
        self.heap.append(item)
        self.__floatUp(len(self.heap)-1)
        
    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1,len(self.heap)-1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        
        elif len(self.heap) == 2:
            max = self.heap.pop()
        
        else:
            max = False
        
        return max
        
    def __swap(self,i,j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def __floatUp(self,index):
        parent = index//2
        if index <=1:
            return 
        else:
            if self.heap[parent] < self.heap[index]:
                self.__swap(parent, index)
                self.__floatUp(parent)
                
    def __bubbleDown(self,index):
        left = 2*index
        right = 2*index + 1
        
        largest = index
        
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)

m = maxHeap([3, 21, 95])            
m.push(10)  
print(m.peek())
print(str(m.heap[0:len(m.heap)]))
print(str(m.pop()))
print(m.peek())
