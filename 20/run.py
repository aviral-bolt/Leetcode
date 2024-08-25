class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashTable = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for c in s:
            if c in hashTable:
                if stack and stack[-1] == hashTable[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

# - list supports LIFO property of stack via append() and pop()
# - to access last element, we can use negative indexes like -1, -2 instead of calc size and finding the actual index count 
# - when c is found in hashtable, then first check if stack is empty or not or else we could be comparing empty stack to a value in our hash table -- giving us index error

# TC - N
# - N is string size (traversal)

# SC - N + k
# - N is string size (stack size)
# - k is number of unique pairs in data (hash table)

class Solution:
    def isValid(self, s: str) -> bool:
        low = 0
        high = len(s)-1

        hashTable = {
            '(':')',
            '[':']',
            '{':'}'
        }

        while low < high:
            if s[high]!= hashTable[s[low]]:
                return False
            else:
                low += 1
                high -= 1
        
        return True

# fails for test case - "()[]{}" - as this input is not symmetrical which is a property needed for two pointer to work 