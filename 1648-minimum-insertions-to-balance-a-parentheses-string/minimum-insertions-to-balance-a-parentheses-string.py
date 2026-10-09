class Solution:
    def minInsertions(self, s: str) -> int:
        count=0
        i=0
        res=0
        while i<len(s):
            if s[i]=='(':
                count+=1
                i+=1
            else:
                if count>0:
                    count-=1
                else:
                    res+=1

                if i<len(s)-1 and s[i+1]==')':
                    i+=2
                else:
                    res+=1
                    i+=1


        return res + (count*2)                     