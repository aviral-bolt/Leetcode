# Link - https://leetcode.com/problems/contains-duplicate/

## Intuition 
- need to find only duplicate occurence to return true
- array has integer datatype 

## Approach

### Sorting 
- sort the array 
- compare consecutive elements and if they match, a duplicate is found

### Hashing
- create a data structure to store each element
- when an element already exists in ds, duplicate found