class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs, seen = 0, []
        for num in nums:
            if num in seen:
                pairs += seen.count(num)
            seen.append(num)
        return pairs