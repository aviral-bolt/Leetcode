# Link - https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

## Intuition 
- polish notation means first operands are there, then operators follows
- we insert the reverse order of array elements into the stack ds
- then we can pick out a group and do the calculations 
- this method of notation allows to evaluate expression in linear manner aka does not need brackets n all (which is commonly seen and is called infix notation)

## Approach 
- run a loop to get each token 
- check if the token is non operator and add it to stack
- if token is an operator then pop previous token from stack and person that operator on them 
- after calculation, push the updated token into the stack and move to next token via loop 