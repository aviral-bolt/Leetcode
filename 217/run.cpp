class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        
        for (int i=0; i<nums.size()-1; i++){
            if(nums[i]==nums[i+1]){
                return true;
            }
        }
        return false
    }
};

// Sorting
// inplace solution but constant space
// TC can be improved to linear

// TC - N log N; vector size, sort function
// SC - 1

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> hash;

        for(int i=0; i<nums.size(); i++){
            if(hash.find(nums[i])!=hash.end()){
                return true;
            }
            hash.insert(nums[i]);
        }
        return false;
    }
};

// Hashing
// not inplace solution 

// TC - N - vector size, traversal
// SC - N - vector size, hash when no duplicates found