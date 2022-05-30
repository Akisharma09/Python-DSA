
def mergeSortedArrays(a,b):
    i = 0
    j = 0
    sorted_array = []
    
    while (i < len(a) and j < len(b)):
        if(a[i] <= b[j]):
            sorted_array.append(a[i])
            i+=1
        else:
            sorted_array.append(b[j])
            j+=1
    
    while i < len(a):
        sorted_array.append(a[i])
        i+=1
    while j < len(b):
        sorted_array.append(b[j])
        j+=1
        
    return sorted_array

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    
    left = mergeSort(left)
    right = mergeSort(right)
    
    sorted_array = mergeSortedArrays(left, right)
    
    return sorted_array
            

def swap(arr,a,b):
    arr[a], arr[b] = arr[b], arr[a]

def bubbleSort(arr):
    ctr = len(arr)-1
    while (ctr != 0):
        for j in range(ctr):
            if arr[j+1] > arr[j]:
                j += 1
            else:
                swap(arr,j,j+1)
        
        ctr -=1

def partition(arr,start,end):
    
    pivot_index = start
    pivot = arr[start]
    
    while start < end:
        
        while start < len(arr) and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        
        if start < end:
            swap(arr,start,end)
        
    swap(arr,pivot_index,end)
    
    return end

def lomutoPartition(arr,lo,hi):
    pivot = arr[lo]
    current = lo
    
    for i in range(lo+1,hi+1):
        if arr[i] < pivot:
            current +=1
            swap(arr,current,i)
    
    swap(arr,current,lo)
    
    return current
    

def quickSort(arr,start,end):
    if start < end:
        pi = partition(arr,start,end)
        quickSort(arr, start, pi-1) # left
        quickSort(arr, pi+1, end) # right
        
def quickSortlo(arr,start,end):
    if start < end:
        pi = lomutoPartition(arr,start,end)
        quickSort(arr, start, pi-1) # left
        quickSort(arr, pi+1, end) # right


def insertionSort(arr):
    for i in range(1,len(arr)-1):
        anchor = arr[i]
        j = i-1
        while j >= 0 and arr[j]> anchor:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = anchor
    
    return arr
    

if __name__ == '__main__':
    elements = [11,9,29,38,2,15,28]
    bubbleSort(elements)
    print('Bubble sort result is: {}'.format(elements))
    
    elements = [11,9,29,38,2,15,28]
    quickSort(elements,0,len(elements)-1)
    print('quick sort result is: {}'.format(elements))
    
    elements = [11,9,29,38,2,15,28]
    quickSortlo(elements,0,len(elements)-1)
    print('quick sort lomuto result is: {}'.format(elements))
    
    elements = [11,9,29,38,2,15,28]
    elements = insertionSort(elements)
    print('insertion sort result is: {}'.format(elements))
    
    elements = [11,9,29,38,2,15,28]
    elements = mergeSort(elements)
    print('merge sort result is: {}'.format(elements))
