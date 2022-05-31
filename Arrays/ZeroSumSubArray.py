"""
Approach:
    cummulative sum in hashmap is zero return index
"""

def findZeroSum(arr):
    hashmap = {}
    cumm_sum = 0
    for i in range(len(arr)):
        cumm_sum += arr[i]
        if cumm_sum in hashmap:
            return (hashmap[cumm_sum]+1, i)
        else:
            hashmap[cumm_sum] = i
        
    return -1

if __name__ == '__main__':
    arr = [1, 4, -2, -2, 5, -4, 3]
    print(findZeroSum(arr))
