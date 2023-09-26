class Solution {
public:
    int minimumLength(string s) {
        int n= s.length();
        int prefptr=0;
        int sufptr=n-1;
        while(s[prefptr]==s[sufptr]&&prefptr<sufptr){
            while((prefptr+1)<n && s[prefptr]==s[prefptr+1])
                prefptr++;
            while((sufptr-1) >=0 && s[sufptr] == s[sufptr-1])
                sufptr--;
            
            if(prefptr>=sufptr){
                return 0;
            }
            else{
                prefptr++;
                sufptr--;
            }
        }
        return sufptr-prefptr+1;
    }
};