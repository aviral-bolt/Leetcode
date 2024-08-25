# Link - https://leetcode.com/problems/valid-parentheses/description/

## Intuition 
- there are three types of brackets in input 
- we need to ensure count of each type is equal aka all get closed
- we also need to ensure that order of closing is correct aka if higher priority bracket is open then a lower priority bracket cannot be closed before. But we can open brackets in any order. 
- actually its not about priority, its about the sequence in which brackets were opened and in same sequence they must be close aka they input is a mirror and can be solved right away with two pointers approach
- but wait, what if some bracket is opened and closed in linear sequence and not concentric sequence. In this case, the mirror property can be applied to solve the problem
- a hint of using stack ds for this 

- how is list used as stack in python? 


## Approach
- set low pointer to 0 and high to size-1
- at each step, bring them closer by 1 index
- at each step check if they are equal to determine that closing order is correct
---
- create a stack ds to ensure order
- create a hashtable to ensure correct matching
- loop over the string and for open brackets, add them to stack and for close brackets, check if there is opening bracket in stack and remove it if that opening bracket is in correct place
- correct place of opening bracket is right before it 

##