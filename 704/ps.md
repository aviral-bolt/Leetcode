# Link - https://leetcode.com/problems/binary-search/description/

## Intuition 
- the array is sorted 
- we have to search a target, so sort + search = binary search 

## Approach 
- set a low and high pointer 
- loop until low is less than high 
- inside loop we calc mid of these pointer and compares it value with the target 
- if target is lower than mid then we reduce high pointer position 
- if target is higher than mid then we increase low pointer position 