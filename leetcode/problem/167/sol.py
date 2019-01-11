class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
# use dictionary

        dic = {}
        for i,number in enumerate(numbers):  
            if number in dic:
                return (dic[number],i+1)
            else:
                dic[target-number] = i+1
                
                
               
