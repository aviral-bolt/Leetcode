class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = len(numbers)-1
        diff = 0

        while low < high:
            diff = target - numbers[low]
            if diff == numbers[high]:
                return list([low+1, high+1])
            elif diff > numbers[high]:
                low += 1
            else:
                high -= 1

# TC - N 
# - vector size (traversal)

# SC - 1 