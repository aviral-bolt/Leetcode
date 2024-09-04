# Link - https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

## Intuition 
- we can give inplace solution 
- brute way will be to create a hashset and then overwrite the set elements onto the array 
- optimal way is to use two pointers where second pointers finds the next unique element and is copied to position of first pointer 