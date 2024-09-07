#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    // Function to find floor of x
    // n: size of vector
    // x: element whose floor is to find
    int findFloor(vector<long long> &v, long long n, long long x) {

        // Your code here
        long long low =0;
        long long high = n-1;
        int ans = -1;
        
        while (low <=high){
            long long mid = low + ((high-low)/2);
            if (v[mid]<=x){
                ans = mid;
                low = mid+1;
            }
            else {
                high = mid-1;
            }
        }
        return ans;
    }
};

// TC - log N (binary search)
// SC - 1 
