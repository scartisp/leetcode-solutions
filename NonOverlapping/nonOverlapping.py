class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        start = intervals[0][0]
        end = intervals[0][1]
        interval = abs(end-start)
        count = 0

        for i in range(1, len(intervals)):
            startTwo = intervals[i][0]
            endTwo = intervals[i][1]
            intervalTwo = abs(endTwo-startTwo)
            if start < endTwo and startTwo < end:
                count += 1
                if end > endTwo:
                    start = startTwo
                    end = endTwo
                    interval = intervalTwo
            else:
                start = startTwo
                end = endTwo
                interval = intervalTwo
        
        return count
