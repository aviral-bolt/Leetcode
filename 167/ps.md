# Link - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

## Intuition
- numbers are sorted in ascending order, so if we pick first number then we just have to find the diff in rest of the array 
- since only one solution exists, we can exit on finding the pair via return statement
- input and output array are having 1-based indexing 
- we can use two loops to find the pair 
- or we can use two pointers to do it in one loop itself, and use the ascending property of the question 

## Approach 
- set a low pointer and compare its diff with high pointer
- if high is bigger than diff then we reduce high to find again for our selected low 
- if high is smaller than diff then we know a pair can't be made with that low. we increase low by 1 index then
- but what if we keep on reducing high for a low and then when we move to next low, our high has skipped places based prev low? should be fine because we have next low will still not satisfy those skipped highs

## Footnotes
- we can use binary search to find the diff but its TC will increase to N log N 
- we can use dictionary to hash and then find diff in constant time but its SC will increase to N 