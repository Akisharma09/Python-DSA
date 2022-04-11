#Rotate Array of size N by D times anti clock wise(left)
'''
Idea is to to move elements in set and the size of set is gcd of N and D.

For array of size 12 and number of rotation as 3 (N=12, D=3) gcd(12,3) is 3. so set size will be 3, thus we will be moving three element at a time.
gcd is gratest common devisor
'''
    def rotateArr(self,A,D,N):
        #Your code here
        def gcd(a, b):
            if b == 0:
                return a;
            else:
                return gcd(b, a % b)
            
        D = D%N
        gratest_common_devisor = gcd(D,N)
        
        for i in range(gratest_common_devisor):
            temp = A[i]
            j = i
            while 1:
                k = j+D
                if k>=N:
                    k = k-N
                if k == i:
                    break
                A[j] = A[k]
                j = k
                A[j] = temp
        
        return A
      
      
#Approach2:
'''
Reverse first D elements 
Then Reverse N-D elemnts remaining
Then Reverse te entire Array
'''

def rotateArr(self,A,D,N):
        #Your code here
        D = D%N
        def reverse(arr,start,end):
            while start<end:
                arr[start], arr[end] = arr[end], arr[start]
                start +=1
                end -=1
        
        reverse(A,0,D-1)
        reverse(A,D,N-1)
        reverse(A,0,N-1)
        
        return A

'''
Approach 3

use list slicing
'''
def rotateArr(self,A,D,N):
        #Your code here
        D = D%N
        A[:] = A[D:N]+A[0:D]
        return A
