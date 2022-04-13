'''
Approach
'''


def maxIndexDiff(arr, n):
    maxDiff = -1
    for i in range(n):
        j = n-1
        while (j>i):
            if(arr[j] > arr[i]):
                maxDiff = max(maxDiff,j-i)
            else:
                j -= 1
        
    return maxDiff

def main():
    arr = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
    n = len(arr)
    maxDiff = maxIndexDiff(arr, n)
    print(maxDiff)

if __name__ == '__main__':
    main()



'''
i is from 0 
j is from end
'''

# For a given array arr[], 
#   returns the maximum j – i such that
#   arr[j] > arr[i] */
def maxIndexDiff(arr, n):
     
    leftMin = [0]*n
    leftMin[0] = arr[0]
    for i in range(1,n):
        leftMin[i] = min(leftMin[i-1], arr[i])
         
    # leftMin[i] = min arr[0...i] 
    maxDist = - 2**32
    i = n-1
    j = n-1
     
    while(i>=0  and  j>=0):
         
        if(arr[j] >= leftMin[i]):
            maxDist = max(maxDist, j-i)
            i-=1
        else:
            j-=1
             
    return maxDist
 
# Driver Code
arr = [34,8,10,3,2,80,30,33,1]
n = len(arr)
maxDiff = maxIndexDiff(arr, n)
print(maxDiff)
