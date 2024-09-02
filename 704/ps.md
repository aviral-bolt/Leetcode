# Link - https://leetcode.com/problems/binary-search/description/

## Intuition 
- the array is sorted 
- we have to search a target, so sort + search = binary search 
- if mid is not equal to target, high = mid -1 and not mid 
- the moment mid = target, our search is complete, irrespective of leftover search space 
- when target does not exist, the high will go behind low due to high = mid -1 and that is when condition breaks and search ends
- low == high is a possibility with leftover search space, so low > high is not the breaking condition 

## Approach 
- set a low and high pointer 
- loop until low is less than high 
- inside loop we calc mid of these pointer and compares it value with the target 
- if target is lower than mid then we reduce high pointer position 
- if target is higher than mid then we increase low pointer position 