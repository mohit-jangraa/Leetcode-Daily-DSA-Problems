class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                d= {}
                k=i
                while k<=j:
                    if nums[k] not in d:
                        d[nums[k]]=1
                    k+=1
                res+=(len(d.keys())**2)

        return res        
                         
                        
