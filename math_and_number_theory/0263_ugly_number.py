class Solution:
    def isUgly(self, n: int) -> bool:
        factors = {2, 3, 5}
        divider = 2
        while divider * divider <= n:
            while n % divider == 0:
                if divider not in factors:
                    return False
                n //= divider
            divider += 1
        return n == 1 or n in factors
