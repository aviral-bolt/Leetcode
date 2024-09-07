//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User code template

class Solution {
  public:
    vector<int> getFloorAndCeil(int x, vector<int> &arr) {
        // code here
        sort(arr.begin(), arr.end());
        
        int low =0;
        int high =arr.size()-1;
        
        int floor = -1;
        int ceil = -1;
        
        while (low <=high){
            int mid = low + ((high-low)/2);
            
            if (arr[mid] < x){
                floor = arr[mid];
                low = mid+1;
            }
            else if (arr[mid] ==x) {
                floor = arr[mid];
                ceil = arr[mid];
                break;
            }
            else{
                ceil = arr[mid];
                high = mid-1;
            }
        }
        return {floor, ceil};
    }
};

// TC - log N (binary search)
// SC - 1