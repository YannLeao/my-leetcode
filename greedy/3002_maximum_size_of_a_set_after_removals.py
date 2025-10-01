from typing import List


class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        k = n // 2

        set1 = set(nums1)
        set2 = set(nums2)

        common = set1 & set2
        only_1 = set1 - set2
        only_2 = set2 - set1

        take_1 = min(len(only_1), k)
        take_2 = min(len(only_2), k)

        remaining_1 = k - take_1
        remaining_2 = k - take_2

        take_common = min(len(common), remaining_1 + remaining_2)
        return take_1 + take_2 + take_common
