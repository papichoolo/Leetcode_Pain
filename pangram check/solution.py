class Solution(object):
    def checkIfPangram(self, sentence):
        lis='qwertyuiopasdfghjklzxcvbnm'
        l=[]
        for i in lis:
            l.append(i)
        k=[]
        for j in sentence:
            k.append(j)

        m=set(l)
        n=set(k)
        if(len(m.difference(n))==0):
            return True
        else:
            return False


        """
        :type sentence: str
        :rtype: bool
        """
        