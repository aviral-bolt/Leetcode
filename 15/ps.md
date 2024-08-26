# Link - https://leetcode.com/problems/3sum/

## Intuition 
- triplets are having sum = 0 and have distinct indexes 
- we can select any two and then try to find the third one. data is not sorted so binary search can't be done 

## Approach 
- we loop over nums to pick 1 element as our first number 
- we then use two pointers to find the rest two numbers 
- when a triplet is found, we avoid further duplicates by checking next pointer values to current ones 