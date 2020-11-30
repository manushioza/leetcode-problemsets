# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums
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

# Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.
# For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of
# candies among them. Notice that multiple kids can have the greatest number of candies.


class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        l = []
        # Checks if adding candy will result new candy number being the mx number in list
        for i in range(len(candies)):
            candies[i] += extraCandies
            if(max(candies) == candies[i]):
                l.append(True)
            else:
                l.append(False)
            candies[i] -= extraCandies
        return l
