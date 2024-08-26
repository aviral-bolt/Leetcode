class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens: 
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else: 
                stack.append(int(c))
        return stack[0]

# - notice how appending of number is reversing their order in stack wrt list - this is why we need to reverse for minus and divide operations 
# - to satisfy rounding towards zero for negative division, we just typecast it to int datatype (default is float datatype for division)

# TC - N 
# - N is list size (traversal) 

# SC - 3
# - maximum variables at one point 