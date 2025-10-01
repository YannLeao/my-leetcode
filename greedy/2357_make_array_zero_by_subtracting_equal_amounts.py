from typing import List

# Greedy Solution
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(nums) - {0})

# class Solution:
#     def minimumOperations(self, nums: List[int]) -> int:
#         operations = 0
#         while any(nums):
#             choose = min(num for num in nums if num > 0)
#             nums = [num - choose if num > 0 else 0 for num in nums]
#             operations += 1
#         return operations
