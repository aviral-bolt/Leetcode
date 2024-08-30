vector<int> bfs (int V, vector<int> adj[]){
    vector<int> visited(adj.size(), 0)
    queue q;

    visited[0] = 1  // since 1 based indexing of nodes 
    queue.push(V)

    vector<int> ans

    while(!q.empty()){
        int node = q.front()
        q.pop()

        ans.push_back(node)
        for (auto it : adj){
            if (!visited[it]){
                visisted[it] = 1
                q.push(it);
            }
        }
    }
    return ans
}

// TC - N * 2E
// - N is count of nodes (traversal via queue pop)
// - E is number of edges in graph (calc number of neighbours traversed overall)
// - n is multipled by 2e because worst case is when one node has all other nodes as neighbours 

// SC - N + N + N 
// - N is number of nodes - queue ds, visited array, store ans 