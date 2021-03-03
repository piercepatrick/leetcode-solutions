class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {num: i for i, num in enumerate(nums)}
        
        for i, num in enumerate(nums):
            if (j := num_index.get(target-num)) and i != j:
                    return [i, j]