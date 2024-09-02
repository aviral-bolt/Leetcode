class Solution {
  public:
    int largest(vector<int> &nums) {
        // code here
        int largest = INT_MIN;
        for (int i=0; i<nums.size(); i++){
            if (nums[i] > largest){
                largest = nums[i];
            }
        }
        return largest;
    }
};

// TC - N 
// SC - 1 