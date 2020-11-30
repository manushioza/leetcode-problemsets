# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).Return the running sum of nums
# Run Time = 20 ms
# Memory Usage = 13.6 MB

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Loops through rang of 1 to length of i and adds previous value to current value to get sum
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
