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
