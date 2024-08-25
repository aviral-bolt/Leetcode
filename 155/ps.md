# Link - https://leetcode.com/problems/min-stack/

## Intuition
- stack can be implemented using a list in python as it has functions for LIFO property
- the main thing in this question is how we can get the minimum value in a stack in constant time 
- we can create another stack that stores min value upto that point and then use its topmost value as the minimum value of our main stack 
- we have to create a stack for tracking min value and not just a single variable because there is pop function which could remove our current minimum value, and then how do we know what was the minimum value before that? 
- for storing mins as stack is updated, we can use maps also and keep count of repeated values instead of storing separately as we did in stack. but this optimization is not worth it and probably list is less resource intensive than a dictionary in python 

## Approach
- create a normal stack 
- create a min stack and during each push operation, compare the value to current min and store the most min element. this elements location is next to our normal stack only 

##