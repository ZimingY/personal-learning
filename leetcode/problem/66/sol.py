class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        l = len(digits)
        for i in range(l):
            num = digits[l-i-1] * pow(10,i) + num
        return [int(i) for i in str(num+1)]
