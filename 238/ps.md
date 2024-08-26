# Link - https://leetcode.com/problems/product-of-array-except-self/

## Intuition 
- It product of all elements except the current element 
- I can find the total product and then for each element, divide it by the element to form our product array 
- there is some multiplication property that i  can use 

## Approach
- create a list having prefix product for each index
- then loop again in reverse order and calculate postfix product for each index. 
- for each index, we can find its product value by multiplying its prefix product and postfix product 