'''
Given an unsorted array arr[] of N integers and a sum. The task is to count the number of subarrays which add to a given number.
'''

class Solution:
    def findSubarraySum(self,arr, n, Sum):  
        #code here
        current_sum = 0
        number_of_sub_arrays = 0
        map = {0:1}
        
        for elements in arr:
            current_sum += elements
            
            if (current_sum - Sum) in map:
                number_of_sub_arrays += map[current_sum - Sum]
               
            if (current_sum not in map):
                map[current_sum] = 1
            else:
                map[current_sum] +=1
            
        return number_of_sub_arrays
