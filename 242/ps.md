# Link - https://leetcode.com/problems/valid-anagram/description/

## Intuition 
- anagrams are strings with same character but in different order 
- can characters repeat differently? no
- when size is not equal we can directly return false. Duplicates values are also same in an anagram. 

## Approach

**Sorting**
- check equal size
- sort the strings and compare each element 
- is anagram when traversal is completed of both strings 

**Hashing**
- store count of each unique element in a hash 
- if all counts are same then they are anagram

## Idea 
- we use a pair for data and its count, so we use unordered_map, rather than unordered_map
- in python, we can't directly increment because for first occurence of a char, it gives key error instead of automatically creating a key and initializing it 