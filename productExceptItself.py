    def productExceptSelf(self, nums, n):
        #code here
        prod = []
        temp = 1
        for i in range(n):
            prod.append(temp)
            temp *= nums[i]
        
        temp = 1
        for i in range(n-1,-1,-1):
            prod[i] *= temp
            temp *= nums[i]
        
        return prod
 

'''
Approach 2 is using logs:
x = a*b*c*d
log x = log(a)+log(b)+log(c)+log(d)
x = antilog(log(a)+log(b)+log(c)+log(d))

now to find product without itself is 
sum = 0
for i in array:
    sum += log(i)
prod_without_b = antilog(sum of logs - log(b))
'''

import math
 
# epsilon value to maintain precision
EPS = 1e-9
 
def productPuzzle(a, n):
    
    # to hold sum of all values
    sum = 0
    for i in range(n):
        sum += math.log10(a[i])
     
    # output product for each index
    # antilog to find original product value
    for i in range(n):
        print (int((EPS + pow(10.00, sum - math.log10(a[i])))),end=" ")
     
    return
  
# Driver code
a = [10, 3, 5, 6, 2 ]
n = len(a)
print ("The product array is: ")
productPuzzle(a, n)



'''
Approach 3 

As we know a/b is equivalent to a*(b**-1) so using this :

prod = 1
for i in array:
    prod *= i

for i in array:
    print(prod*(i**-1), end = " ")

'''


def solve(arr, n):
 
    # Initialize a variable to store the
    # total product of the array elements
    prod = 1
    for i in arr:
        prod *= i
 
    # we know x / y mathematically is same
    # as x*(y to power -1)
    for i in arr:
        print(int(prod*(i**-1)), end =" ")
 
# Driver Code
arr = [10, 3, 5, 6, 2]
n = len(arr)
solve(arr, n)
