class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int low =0;
        int high = nums.size()-1;
        int ans = nums.size();

        while (low <= high){
            int mid = low + (high-low)/2;
            if (nums[mid] == target){
                return mid;
            }
            else if (nums[mid] >= target){
                ans = mid;
                high = mid-1;
            }
            else{
                low = mid+1;
            }
        }
        return ans;
    }
};

// - if smallest value is also greater than target, then 2nd condition will take care of it by ans = mid = 0

// TC - log N (binary search)
// SC - 1 