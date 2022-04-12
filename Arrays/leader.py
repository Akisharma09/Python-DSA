"""
Idea is to travesre list from behind and print or push all leaders to new list
"""
def leaders(self, A, N):
        #Code here
        leader = []
        leader.append(A[N-1])
        l = leader[0]
        for i in range(N-2,-1,-1):
            if l <= A[i]:
                leader.append(A[i])
                l = A[i]
        return leader[::-1]
