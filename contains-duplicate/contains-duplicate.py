class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        
        if (len(nums) == 1): return False
        
        for i, num in enumerate(nums):
            if (num == nums[i-1]):
                return True
            
        return False
            
            