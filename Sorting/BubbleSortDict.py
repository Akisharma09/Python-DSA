"""
Bubble sort
Approach: compare two adjacent elements if one is grater than other than swap
else move to next element and compare the next two, Do this for all the
elements.
"""

def bubbleSort(element, key):
    len_list = len(element)
    while(len_list != 0):
        for i in range(0,len_list-1):
            if element[i][key] > element[i+1][key]:
                element[i], element[i+1] = element[i+1], element[i] 
        len_list -= 1
        print(element)    
        
    return element


elements = [{'name': 'akshay', 'amount': 5000, 'device': 'oneplus'}
            ,{'name': 'aditya', 'amount': 2000, 'device': 'samsung'}
            ,{'name': 'apar', 'amount': 3000, 'device': 'iphone'}
            ,{'name': 'arpan', 'amount': 4000, 'device': 'moto'}]

sorted_elements = bubbleSort(elements, 'amount')
print('')
print('')
print('')
print('elements in sorted order are: {}'.format(sorted_elements))
