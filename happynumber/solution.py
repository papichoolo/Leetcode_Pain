class Solution:
    def isHappy(self, n: int) -> bool:
        bruh= set()
        #unhappy nos. will have LL cycle in other number than 1, 2
        while n not in bruh:
            bruh.add(n)
            n=self.addsq(n)
            if n==1:
                return True

        return False
    def addsq(self, n):
        rem=0
        ans=0
        while(n!=0):
            rem=n%10
            ans+=rem**2
            n=n//10
        return ans

    