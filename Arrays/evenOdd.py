def segregateEvenOdd(self,arr, n):
		# code here
		l = 0
		r = n-1
		while l<r:
		    while (arr[l]%2 == 0 and l < r):
		        l+=1
		    while (arr[r]%2 != 0 and l<r):
		        r-=1
		    arr[l],arr[r] = arr[r],arr[l]
		
	    return arr
