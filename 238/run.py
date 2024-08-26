class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans = [1]* (len(nums))
        postfix = 1

        for i in range(1, len(nums)):
            ans[i]= ans[i-1] * nums[i-1]
        
        for i in range(len(nums)-1, -1, -1):
            ans[i] = postfix * ans[i]
            postfix = postfix * nums[i]

        return ans

# - notice how range is used to accomodate 0 based indexing for num values and also a -1 offset for prefix values
            

# TC - 2 N 
# - N is list size (traversal, two pass)

# SC - N
# - N is list size (stores prefix products and then later on, stores ans)