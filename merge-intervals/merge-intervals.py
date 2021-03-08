class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        final = []
        intervals = sorted(intervals)
        for i,interval in enumerate(intervals):
            if final and interval[0] <= final[-1][1]:
                final[-1][1] = max(final[-1][1], interval[1])
            
            else: 
                final.append(interval)
        return final

