"""
Quick Sort 

put pivot element(1st element) at right place i.e. all elements towards right
are grater than pivot and all on the left to it are smaller. 
[11,9,2,7,29,15,28]
"""

    
def swap(arr,start,end):
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp

def partition(arr,start,end):
    pivot_index = start
    
    while start < end:
        while start < len(arr) and arr[start] <= arr[pivot_index]:
            start +=1
        
        while arr[end] > arr[pivot_index]:
            end -= 1
            
        if start < end:
            swap(arr,start,end)
    
    swap(arr,pivot_index,end)
    
    return end
        
def quickSort(arr,start,end):
    
    if start < end:
        pi = partition(arr,start,end)
        quickSort(arr,start,pi-1)
        quickSort(arr,pi+1,end)
    

if __name__ == '__main__':
    elements = [11,9,2]
    quickSort(elements,0,len(elements)-1)
    print(elements)
