from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        [1]
        [1,2]
        [1,3,2]
        [1,3,2,4]
        [1,3,2,5,4]
        [1,3,2,5,4,6]
        [1,3,2,5,4,7,6]
        [1,3,2,5,4,7,6,8]
        ...
        """
        # [1,1,2,2,3,3]
        # [2,3,1,3,1,2]
        # [1,2,1,3,2,3]
        newNums = [num for num in nums]
        newNums.sort()
        n = len(nums)
        small = newNums[:(n + 1) // 2][::-1]
        big = newNums[(n + 1) // 2:][::-1]
        for i in range(n):
            if i % 2 == 0:
                nums[i] = small[i // 2]
            else:
                nums[i] = big[i // 2]
