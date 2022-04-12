def hasArrayTwoCandidates(self,arr, n, x):
		# code here
		hash_map = {}
		for i in arr:
		    if (x-i in hash_map):
		        return True
		    hash_map[i]=1
		
		return False
