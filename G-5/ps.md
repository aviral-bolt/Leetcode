# Link - https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1

## Intuition 
- we are provided a adjacency list and a starting node
- nodes are 1 based indexed 
- we can put the starting node into queue ds and then we find its neighbors using adjacency list
- in bfs, we are essentially doing level order traversal and neighbors are actually the next level of current node 
- also, since graphs can be cyclic, we need to do level order traversal and keep track of visited nodes, which is what we are called BFS here

## Approach
- initialize a visited array with 0 
- push starting node into queue ds 
- push all neighbouring nodes into the queue 
- move onto next node present at front of our queue ds 