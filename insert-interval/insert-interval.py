class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        final = []
        n = newInterval
        for index, i in enumerate(intervals):
            if i[1] < n[0]:
                final.append(i)
            elif n[1] < i[0]:
                final.append(n)
                return final+intervals[index:]
            else: 
                n[0] = min(n[0], i[0])
                n[1] = max(n[1], i[1])
        final.append(n)
        return final