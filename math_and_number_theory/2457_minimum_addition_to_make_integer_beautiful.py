class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def digit_sum(x: int):
            return sum(int(d) for d in str(x))

        if digit_sum(n) <= target:
            return 0

        original = n
        base = 1
        while digit_sum(n) > target:
            n = (n // base + 1) * base
            base *= 10
        return n - original
