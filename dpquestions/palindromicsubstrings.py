#this is a problem to count the number of palindromic substrings in a given string

class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0

        #for odd palindromes
        for i in range(len(s)):
            l = r= i
            while l>=0 and r<len(s) and s[l]==s[r]:
                res+=1
                l-=1
                r+=1
        
        #for even palindromes(considering two characters at a time)
            l=i
            r=i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                res+=1
                l-=1
                r+=1
        return res
    

# Time complexity: O(n^2)
