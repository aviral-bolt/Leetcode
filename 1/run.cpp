class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i=0; i<nums.size(); i++){
            for (int j=i+1; j<nums.size(); j++){
                if (nums[i] + nums [j] ==  target){
                    return {i,j};
                }
            }
        }
        return {-1, -1};
    }
};

// TC - N^2 (traversal)
// SC - 1 

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> mp;
        for (int i=0; i<nums.size(); i++){
            int first = nums[i];
            int delta = target - first;
            if (mp.find(delta) !=mp.end()){
                return {i, mp[delta]};
            }
            mp[nums[i]] = i;
        }
        return {-1, -1};
    }
};

// TC - N (traversal) * log N (map find function)
// SC - N (hashing)

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        sort (nums.begin(), nums.end());
        int left = 0;
        int right = nums.size()-1;
        while (left < right){
            int sum = nums[left] + nums[right];
            if (sum == target){
                return {left, right};
            }
            else if (sum > target){
                right--;
            }
            else {
                left++;
            }
        }
        return {-1, -1};
    }
};

// - inplace solution 

// TC - N log N (sorting) + N (traversal)
// SC - 1 