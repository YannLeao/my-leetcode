from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        sets = map(set, nums)
        intersection = set.intersection(*sets)
        return list(intersection)
