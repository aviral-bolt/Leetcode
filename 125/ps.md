# Link - https://leetcode.com/problems/valid-palindrome/description/

## Intuition
- Palindrome is when after removing non-alphanumeric characters and converting uppercase to lowercase, the resulting string is same to its reverse order
- when converting the input string, we can create two separate strings and check if they are equal or not. this will solve in one pass 
- here order is important, so unordered ds for hashing can not be used 
- converted string is empty, then it is also a palindrome

## Approach 
- run a loop over string 
- low pointer goes from start of string and builds forwards string
- high pointer goes from end of string and builds backwards string
- if they both are equal then it is a palindrome
