# solution 1 with o(n^2) time
from collections import defaultdict

"""
Every time an event starts, the total number of events at that time increases by 1, and when it ends, the number of events decreases by 1.
This algorithm stores the differences in events at given time points, then iterates over them to find the largest the number of events will be 
at across the whole interval.
"""


class MyCalendarThree:

    def __init__(self):
        self.d = defaultdict(lambda: 0)

    def book(self, start: int, end: int) -> int:
        self.d[start] += 1
        self.d[end] -= 1
        counter = 0
        totalMax = 0
        for i in sorted(self.d.keys()):
            counter += self.d[i]
            totalMax = max(counter, totalMax)
        return totalMax
