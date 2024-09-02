class Solution {
  public:
    // Function returns the second
    // largest elements
    int print2largest(vector<int> &arr) {
        // Code Here
        sort(arr.begin(), arr.end());
        for (int i=arr.size()-1; i>0; i--){
            if (arr[i] != arr[i-1]){
                return arr[i-1];
            }
        }
        return -1;
    }
};

// TC - N log N + N 
// - sorting 
// - traversal

// SC - 1 

class Solution {
  public:
    // Function returns the second
    // largest elements
    int print2largest(vector<int> &arr) {
        // Code Here
        int largest = arr[0];
        int sLargest = -1;
        for (int i=0; i<arr.size(); i++){
            if (arr[i] > largest){
                largest = arr[i];
            }
        }
        for (int i=0; i<arr.size(); i++){
            if (arr[i] > sLargest && arr[i] < largest){
                sLargest = arr[i];
            }
        }
        return sLargest;
    }
};

// TC - 2N 
// SC - 1 

class Solution {
  public:
    // Function returns the second
    // largest elements
    int print2largest(vector<int> &arr) {
        // Code Here
        int sLargest = -1;
        int largest = arr[0];
        for (int i=1; i<arr.size(); i++){
            if (arr[i] > largest){
                sLargest = largest;
                largest = arr[i];
            }
            else if (arr[i] < largest && arr[i] > sLargest){
                sLargest = arr[i];
            }
        }
        return sLargest;
    }
};

// TC - N 
// SC - 1 