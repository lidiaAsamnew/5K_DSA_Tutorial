class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        fre = [0] * n   
        for i in range(n):
            count = 0
            for j in range(n):
                if nums[j] < nums[i]:
                    count += 1
            fre[i] = count 
        return fre
