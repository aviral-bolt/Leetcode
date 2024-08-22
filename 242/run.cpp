class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size()!= t.size()){
            return false;
        }
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());

        for(int i=0; i<s.size(); i++){
            if(s[i]!=t[i]){
                return false;
            }
        }
        return true;
    }
};

// inplace solution
// TC can be linear? 

// TC - N log N - string size, sorting function
// SC - 1 


class Solution {
public:
    bool isAnagram(string s, string t) {

        if (s.size()!=t.size()){
            return false;
        }

        unordered_map<char, int> first;
        unordered_map<char, int> second;

        for(int i=0; i<s.size(); i++){
            first[s[i]]++;
            second[t[i]]++;
        }

        for (int i=0; i<first.size(); i++){
            if (first[i]!=second[i]){
                return false;
            }
        }
        return true;
    }
};

// TC - 2N - string size, traversal
// SC - 2N - string size, hash
