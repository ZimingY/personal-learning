## my solution
class Solution:
    def searchInsert(self, nums, target):
        point = 0
        for i in range(len(nums)):
            if nums[i]==target:
                point = i
                break
            elif nums[i]>target:
                    point = i-1
                    break
        return point
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        
## top solution
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """       
        return len([x for x in nums if x<target])
