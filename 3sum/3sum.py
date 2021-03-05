class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        final = []
        
        if len(nums) < 3:
            return final
        
        for i, num in enumerate(nums[:-2]):
            low = i + 1
            high = len(nums) -1
            target = 0 - num
            while (low < high):
                if nums[low] + nums[high] == target:
                    if [nums[i],nums[low], nums[high]] not in final:
                        final.append([nums[i],nums[low], nums[high]])
                    low += 1
                elif nums[low] + nums[high] > target:
                    high -= 1
                else: 
                    low += 1
        
        return final
        