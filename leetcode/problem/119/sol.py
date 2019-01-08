class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        tri =  [1]*(rowIndex+1)
        for i in range(1,rowIndex):
            tri[i] = int(tri[i-1]*(rowIndex - i + 1)/i)
        return tri

    
    
# in nth row, we have a list: [1, a(1), a(2),..., a(n)]

# a(k+1)  = a(k)*(n-k)/(k+1)
