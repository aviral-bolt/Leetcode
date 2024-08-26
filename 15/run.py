class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        n = len(nums)

        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    threeSum = nums[i] + nums[j] + nums[k]
                    if threeSum == 0:
                        ans.add((nums[i], nums[j], nums[k]))
        return ans

# - set handles the requirements of having unique triplets which this brute force looping will create
# - set ds used add() instead of append() 


# TC - N^3 
# - N is list size (traversal)

# SC - N 
# - N is unique triplets to store ans 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i, a in enumerate (nums):
            if i>0 and nums[i]==nums[i-1]:
                continue

            left = i+1
            right = len(nums)-1
            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum > 0:
                    right -=1
                elif threeSum < 0:
                    left +=1
                else:
                    ans.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left]==nums[left-1] and left < right:
                        left += 1
                    while nums[right]==nums[right+1] and left < right:
                        right -=1
        
        return ans

# - we can use set ds to store ans and skip duplicate duplicates but that increases space complexity if ans is required to a be list of list

# - input has duplicates and we don't want to create triplets with duplicate values, even if they are from distinct indexes - so we are sorting
# - similarly, we increment left and right also to skip duplicates 
# - instead of finding diff and then sum of left, right - this threeSum is simpler way to check if triplets satisfy our 0 sum requirement

# TC - N^2 + N log N 
# - N is list size (traversal in two levels)
# - N is list size (sorting)

# SC - 1
# - not counting ans space
# - sorting libraries take some space which are not factoring