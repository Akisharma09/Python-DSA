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
