class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        
        return False

# TC - N^2
# - N is list size

# SC - 1

class Solution:

    def binarySearch(target: int, nums: List[int]) -> bool:
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (int) (low + ((high - low)/2))
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                low = mid+1
            else: 
                high = mid-1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROW = len(matrix)
        COL = len(matrix[0])

        for i in range(ROW):
            if matrix[i][0] <= target and matrix[i][COL-1] >= target:
               return Solution.binarySearch (target, matrix[i])

        return False

# - we call a function using class name and dot notation (implement encapsulation)
# - equality is used for searching target in each row and assumes duplicates are not existing 
# - low < high is wrong when search space has len = 1


# TC - N + log M 
# - N is row length 
# - M is column length

# SC - 1 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROW = len(matrix)
        COL = len(matrix[0])

        low = 0
        high = ROW * COL -1

        while low <= high:
            mid = (int) (low + ((high-low)/2))
            currRow = (int) (mid / COL)
            currCol = (int) (mid % COL)

            if matrix[currRow][currCol] == target:
                return True
            elif matrix[currRow][currCol] < target:
                low = mid + 1 
            else:
                high = mid - 1
        
        return False

# - note that divide and modulus operator return float which is then typecasted into int as index of a list is of int datatype 
# - to calculate row number of mid pointer, we divide it by col and not by row 

# TC - log N*M 
# - N is number of rows
# - M is number of columns 

# SC - 1 