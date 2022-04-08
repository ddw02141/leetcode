from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = [0 for _ in range(self.n + 1)]
        self.tree = [0 for _ in range(self.n + 1)]
        for i in range(self.n):
            self.update(i, nums[i])
        # print(self.nums)
        # print(self.tree)

    def update(self, index: int, val: int) -> None:
        index = index + 1
        diff = val - self.nums[index]
        self.nums[index] = val
        while index <= self.n:
            self.tree[index] += diff
            index += (index & -index)

    def sumRange(self, left: int, right: int) -> int:
        left = left + 1
        right = right + 1

        return self.prefixSum(right) - self.prefixSum(left - 1)

    def prefixSum(self, index: int) -> int:
        ps = 0
        while index > 0:
            ps += self.tree[index]
            index -= (index & -index)

        return ps

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
