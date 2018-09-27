class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxsum =cursum= nums[0]
        for item in nums[1:]:
            cursum = max(item,cursum + item)
            maxsum = max(maxsum,cursum)
        return maxsum
 

