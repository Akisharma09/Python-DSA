"""
merge sort

Analysis of merge sort: https://www.khanacademy.org/computing/computer-science/algorithms/merge-sort/a/analysis-of-merge-sort
"""


def merge_sort(arr):
    
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    
    sorted_array = merge(left,right)
    
    return sorted_array

def merge(a,b):
    head_a = 0
    head_b = 0
    
    arr = []
    while (head_a < len(a) and head_b < len(b)):
        if a[head_a] <= b[head_b]:
            arr.append(a[head_a])
            head_a +=1
        else:
            arr.append(b[head_b])
            head_b+=1
    
    while head_a <len(a):
        arr.append(a[head_a])
        head_a += 1
    
    while head_b <len(b):
        arr.append(b[head_b])
        head_b += 1
        
        
    return arr

if __name__ == '__main__':
    
    arr = [10,3,15,7,8,23,92,29,100]
    
    print('sorted array is : {}'.format(merge_sort(arr)))
