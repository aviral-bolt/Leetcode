class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]==target):
                    return {i,j}

# TC - N^2 - vector size, traversal
# SC - 1 

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numMap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numMap:
                return [numMap[diff], i]
            numMap[nums[i]] = i

# TC - N - vector size, traversal
# SC - N - vector size, hashing