class Solution {
  public:
    
    void dfs (int node, vector<int> adj[], vector<int> &vis, vector<int> &ans){
        vis[node] = 1;
        ans.push_back(node);
        
        for (auto it : adj[node]){
            if (!vis[it]){
                dfs(it, adj, vis, ans);
            }
        }
    }
    
    vector<int> dfsOfGraph(int V, vector<int> adj[]) {
        // Code here
        vector<int> vis(V, 0);
        vector<int> ans;
        int start = 0;
        
        dfs (start, adj, vis, ans);
        return ans;
    }
};