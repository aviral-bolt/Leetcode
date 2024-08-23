# Link - https://leetcode.com/problems/group-anagrams/

## Intuition
- there are more than 2 anagram elements in the array 
- order does not matter so unordered ds can be used 
- in anagram, characters can have duplicates but they are not repeated
- it is similar to valid anagram questions, but here we are comparing between each string of array instead of each character of string
- characters are in lower case 

## Approach
- for each element, store its ordered characters
- characters can be ordered using sort function 
- then, for each element, find other elements whose ordered characters matches
---
- for each string, sort its characters first
- for first occurence of sorted string, add sorted string as key (we will search for it) and group index of ans where it was appended, as value
- if current string when sorted, is found in our dictionary, then we use dictionary value as ans index and store the current string in unsorted form


## Idea
- keys are unique in dictionary
- ordered dictionary have sorted keys, not sorted values 
- sorted() can sort a string input and return a list, which we can typecast back into string. This function works on all iterable data 

## Advanced
- what if alphanumeric or lower, upper case strings