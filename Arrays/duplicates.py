    def duplicates(self, arr, n): 
    	# code here
    	lst = []
    	for i in range(n):
    	    x = arr[i]%n
    	    arr[x] = arr[x] + n
    	
    	for i in range(n):
    	    if (arr[i]>=2*n):
    	        lst.append(i)
        
        if len(lst) == 0:
            return -1,
        
        return lst
