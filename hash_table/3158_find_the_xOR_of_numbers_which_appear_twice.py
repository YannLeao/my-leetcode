from collections import Counter
from typing import List


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        counts = Counter(nums)
        xor = 0
        for key, value in counts.items():
            if value == 2:
                xor ^= key
        return xor
