class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low <=high:
            mid = (int) ((low + high) / 2) 

            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
        
        return -1

# - instead of explicit typecasting from float to int, we can also use floor division which truncatest the decimal part, thus making it an int 

# TC - log N 
# N is list size 

# SC - 1