class Solution:
    def largest(self, arr : List[int]) -> int:
        # code here
        largest = arr[0];
        for num in arr:
            if num > largest:
                largest = num
        return largest

# TC - N 
# SC - N 