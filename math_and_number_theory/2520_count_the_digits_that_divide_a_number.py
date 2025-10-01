# Pythonic form
class Solution:
    def countDigits(self, num: int) -> int:
        return sum(num % int(d) == 0 for d in str(num))


# class Solution:
#     def countDigits(self, num: int) -> int:
#         sum = 0
#         for val in str(num):
#             if num % int(val) == 0:
#                 sum += 1
#         return sum
