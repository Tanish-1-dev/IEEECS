class IntervalMerger:
    def __init__(self):
        self.intervals = []  # Stores non-overlapping intervals

    def addInterval(self, start: int, end: int):
        new_interval = [start, end]
        merged_intervals = []
        inserted = False
        
        for interval in self.intervals:
            # No overlap, add interval directly
            if interval[1] < start:
                merged_intervals.append(interval)
            elif end < interval[0]:
                if not inserted:
                    merged_intervals.append(new_interval)
                    inserted = True
                merged_intervals.append(interval)
            else:
                # Overlapping intervals, merge them
                start = min(start, interval[0])
                end = max(end, interval[1])
        
        if not inserted:
            merged_intervals.append([start, end])
        
        self.intervals = merged_intervals
    
    def getIntervals(self):
        return self.intervals

# Example Usage
merger = IntervalMerger()
merger.addInterval(1, 5)
merger.addInterval(6, 8)
merger.addInterval(4, 7)
print(merger.getIntervals())  # Output: [[1, 8]]
