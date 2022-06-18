from typing import List


class Solution:

    def __init__(self):
        self.buff4Ptr = 0
        self.buff4Cnt = 0
        self.buff4 = [" " for _ in range(4)]

    def read(self, buf: List[str], n: int) -> int:
        ptr = 0
        while ptr < n:
            if self.buff4Ptr == self.buff4Cnt:
                self.buff4Ptr = 0
                self.buff4Cnt = read4(self.buff4)
                if self.buff4Cnt == 0:
                    break
            buf[ptr] = self.buff4[self.buff4Ptr]
            ptr += 1
            self.buff4Ptr += 1

        return ptr
