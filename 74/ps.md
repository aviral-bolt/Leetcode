# Link - https://leetcode.com/problems/search-a-2d-matrix/description/

## Intuition 
- mxn means m rows and n columns 
- in a row, elements are sorted in increasing order 
- last element of a row is smaller than the first element of next row 
- we can treat it a single row which is sorted and do binary search in it 

## Approach 
- set a low and high pointer to first and last element of matrix 
- if target is higher than mid, then we move low pointer to mid+1 index 
- this mid+1 index is counted by % and / 
- low and high are a linear sequence and not following the matrix's indexes

## Idea 
- duplicates can exist when last element of a row is same as first element. In such case, the solution will give first occurrence of target