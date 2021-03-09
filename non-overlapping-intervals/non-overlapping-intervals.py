class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        close = float('-inf')
        counter = 0
        
        for interval in sorted(intervals, key= lambda x: x[1]):
            if interval[0] >= close:
                close = interval[1]
            else:
                counter += 1
                
        return counter
