"""
Bubble sort
Approach: compare two adjacent elements if one is grater than other than swap
else move to next element and compare the next two, Do this for all the
elements.
"""

def bubbleSort(lst):
    len_list = len(lst)
    while(len_list != 0):
        for i in range(0,len_list-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i] 
        len_list -= 1
        print(lst)    
        
    return lst

unsorted_list = [1,3,12,55,42,13]
sorted_list = bubbleSort(unsorted_list)

print('List in sorted order: {}'.format(sorted_list))
