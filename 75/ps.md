# Link - https://leetcode.com/problems/sort-colors/description/

## Intuition 
- brute is to just use sort function 
- better is to count occurence of 0s, 1s, 2s and then overwrite the array 
- optimal is using dutch national flag algorithm (three pointer types)
    - 0 to low -1 contains 0s
    - low to mid-1 contains 1s
    - high-1 to n-1 contains 2s
    - mid to high is the unsorted space 
    - mid is the reading pointer here 
    - linear TC because for each iteration and its case, the unsorted space gets reduced by 1
