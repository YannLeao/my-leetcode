from collections import Counter
from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c1, c2 = Counter(words1), Counter(words2)
        return len({w for w, cnt in c1.items() if cnt == 1} &
                   {w for w, cnt in c2.items() if cnt == 1})
