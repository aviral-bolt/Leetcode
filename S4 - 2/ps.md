# Link - https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620

## Intuition
- lower bound is first index whose element >= x
- only two possibility of >= or <, instead of 3 in usual binary search 
- can have duplicates, array is sorted 
- STL function exists - lower_bound(arr.begin(), arr.end(), x); 
    - this function return a pointer
    - to get index of that pointer, we do - lower_bound() - arr.begin();