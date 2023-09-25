class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
int cs =0;
int ms =0;
for(int i =0;i<nums.size();i++){
    cs += nums[i];
    if(cs<0){
        cs=0;
    }
    if(cs>ms){
        ms = cs;
    }
}
int cus =0;
int mins =0;
for(int i =0;i<nums.size();i++){
    cus += nums[i];
    if(cus>0){
        cus=0;
    }
    if(cus<mins){
        mins = cus;
    }
}
return max(ms,-mins);
    }
};