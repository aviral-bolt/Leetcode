class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size()-1;
        while (low <= high){
            int mid = low + (high-low)/2;
            if (nums[mid] == target){
                return mid;
            }
            else if (nums[mid] > target){
                high = mid -1;
            }
            else {
                low = mid + 1;
            }
        }
        return -1;
    }
};

// TC - log N 
// SC - 1

class Solution {
public:
    int binarySearch (vector<int> &nums, int low, int high, int target){
        if (low > high){
            return -1;
        }
        int mid = low + ((high-low)/2);
        if (nums[mid] == target){
            return mid;
        }
        else if (nums[mid] > target){
            return binarySearch (nums, low, mid-1, target);
        }
        else {
            return binarySearch (nums, mid+1, high, target);
        }
    }

    int search(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size()-1;
        
        return binarySearch(nums, low, high, target);
    }
};

// TC - log N 
// SC - recursive stack 