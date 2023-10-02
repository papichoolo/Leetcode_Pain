# Check if array is rotated and sorted.

This one is easy, first we have to sort the array using simple sort function, then we have to write a rotate array function, and check for the rotated array matching the given array through each rotation.
```
class Solution {
public:
    void rotate(vector<int> &nums,int k){
        reverse(nums.begin(),nums.begin()+k);
        reverse(nums.begin()+k,nums.end());
        reverse(nums.begin(),nums.end());
    }
    bool check(vector<int>& nums) {
        vector<int> temp=nums;
        sort(temp.begin(),temp.end());
        for(int i=0;i<nums.size();i++){
           vector<int> temp_nums=nums;
            rotate(temp_nums,i);
            if(temp_nums==temp){
               return true;
            }
        }
        return false;
    }
};
```
