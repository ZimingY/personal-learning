
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        tri = list()
        for i in range(numRows):
                tri.append([1]*(i+1))
                if i>1:
                    
                    for j in range(1,i):
                        tri[i][j]  = tri[i-1][j-1] + tri[i-1][j] 
        return tri
