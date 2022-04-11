def majorityElement(self, A, N):
        c = A[0]
        v = 1
        for i in range(1,N-1):
            if c == A[i]:
                v+=1
            elif v == 0:
                c = A[i]
                v = 1
            else:
                v-=1
        cnt = 0
        for i in A:
            if c == i:
                cnt+=1
        
        if cnt>N//2:
            return c
        else:
            return -1
