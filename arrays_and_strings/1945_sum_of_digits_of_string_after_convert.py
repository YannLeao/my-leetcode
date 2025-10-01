class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num_str = "".join(str(ord(c) - ord('a') + 1) for c in s)

        for _ in range(k):
            num_str = str(sum(int(d) for d in num_str))
        return int(num_str)
