"""
Selection sort
"""

def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        if i != min_index:
            arr[min_index], arr[i] = arr[i], arr[min_index] 


if __name__ == '__main__':
    
    elements = [78,12,15,8,61,52,23,27]
    selectionSort(elements)
    print('elements sorted after selection sort: {}'.format(elements))
