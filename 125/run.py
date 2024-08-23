class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res_s = ''
        res_s = ''.join(c for c in s if c.isalnum()).lower()
        return res_s==res_s[::-1]

# list comprehension returns a list which we convert into string

# TC - N + N
# - N is string size (traversal), N is string size (slicing to reverse)
# - isalnum and lower are constant time 

# SC - N + N
# - auxillary space of N (filtered list from list comprehension) 
# - auxillary space of N (reversed string from slicing method)


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left,right = 0, len(s)-1
        while (left < right):
            
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if (s[left].lower() != s[right].lower()):
                return False
            
            left += 1
            right -= 1

        return True

# TC - N/2 
# - N is string size (traversal)

# SC - 1 