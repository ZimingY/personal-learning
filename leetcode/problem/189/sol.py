class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #nums[:] = nums[-k:] + nums[:len(nums)-k]
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]
        
        
# test case nums=[1],k=0, in this case nums[-k:]会output
# 当 n<k, 需要 k % n
