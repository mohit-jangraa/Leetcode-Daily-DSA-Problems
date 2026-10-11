class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        sum = 0
        ans = []
        for ind,i in enumerate(nums):
            if n%(ind+1)==0:
                sum+=(i**2)
                # ans.append(i)

        return sum