	def getXor(self, A, N):
		# code here
		x_o_r = []
		temp = 0
		
		for i in range(N):
		    x_o_r.append(temp)
		    temp ^= A[i]
		
		temp = 0
	
		for i in range(N-1,-1,-1):
		    x_o_r[i] ^= temp
		    temp ^= A[i]
		    
		return x_o_r
