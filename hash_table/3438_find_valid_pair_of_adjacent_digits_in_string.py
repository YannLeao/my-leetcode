from collections import Counter


class Solution:
    def findValidPair(self, nums: str) -> str:
       counts = Counter(nums)
       valid = {char for char, i in counts.items() if int(char) == i}
       for a, b in zip(nums, nums[1:]):
           if (a != b and a in valid and b in valid):
               return a + b
       return ""
