# Link - https://leetcode.com/problems/generate-parentheses/description/

## Intuition 
- from a number of pairs, we can arrange them in ways where opening and closing of a pair is not disturbing the order of another pair 
- to ensure correct order among pairs, we can use stack to track 
- here parenthesis is of only one type so a hashmap wont be needed i guess

## Approach 
- find all combination by backtracking
- base case will be when n parenthesis has been used up 
- for each step, we store add a parenthesis to a stack and then call a func with this updated stack and parenthesis count 
- repeat until all parenthesis are using 