class Solution:
    def removeDuplicates(self, A):
        if not A:
            return 0

        N= 0

        for i in range(1,len(A)):
            if A[N] != A[i]:
                N=N+1
                A[N] = A[i]

        return N+1
                
