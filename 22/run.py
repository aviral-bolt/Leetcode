class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans = [] 

        def backtrackCombination (openN: int, closeN: int):
            if (openN == closeN == n):
                ans.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrackCombination (openN +1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(")")
                backtrackCombination (openN, closeN +1)
                stack.pop()
            
        backtrackCombination(0,0)
        return ans;

# - openN < n not because of 0 based indexing but because we only add until count is less than 1
# - closeN < openN ensures first opening parenthesis are put into stack 

# TC - 2^N 
# - N is number of pairs 

# SC - N 
# - N is height of recursion tree