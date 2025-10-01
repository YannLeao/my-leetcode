class Solution:
    def smallestValue(self, n: int) -> int:
        def sum_primes(x: int) -> int:
            total, divider = 0, 2
            while divider * divider <= x:
                while x % divider == 0:
                    x //= divider
                    total += divider
                divider += 1
            if x > 1:
                total += x
            return total

        new_n = sum_primes(n)
        while new_n != n:
            n = new_n
            new_n = sum_primes(n)
        return n
