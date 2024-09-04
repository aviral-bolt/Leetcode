class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        set<int> st;
        for (int i=0; i<nums.size(); i++){
            st.insert(nums[i]);
        }
        int ind=0;
        for (auto it : st){
            nums[ind] = it;
            ind++;
        }
        return st.size();
    }
};

// TC - N (traversal) + log N (set insertion)
// SC - N (hashing)


class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int pointer = 0;
        for (int i=1; i<nums.size(); i++){
            if (nums[i] > nums[pointer]){
                pointer += 1;
                nums[pointer] = nums[i];
            }
        }
        return pointer+1;
    }
};

// TC - N (traversal)
// SC - 1 