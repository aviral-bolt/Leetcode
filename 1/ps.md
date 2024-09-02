# Link - https://leetcode.com/problems/two-sum/

## Intuition
- more than one answer can exist, but we just have to find first answer
- same element can not be used twice
- duplicate elements can exist
- return the ans in any order means freedom to unordered data structures

## Approach
Traversal
- pick first element and check w all elements 
- pick second element and again try to find its pair 
- no pair found then return false 
---
Hashing
- for each element, stores it diff with target
- find an element which is equal to that diff

