from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_num, xor_range = 0, len(nums)
        for i in range(len(nums)):
            xor_num ^= nums[i]
            xor_range ^= i
        return xor_range ^ xor_num
