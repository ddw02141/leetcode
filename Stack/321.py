from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        len1, len2 = len(nums1), len(nums2)

        def maxList(nums, numLeft):
            drop = len(nums) - numLeft
            stack = list()
            for num in nums:
                while drop > 0 and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:numLeft]

        def merge(n1, n2):
            return [max(n1, n2).pop(0) for _ in range(len(n1) + len(n2))]

        answerList = list()
        for i in range(0, k + 1):
            if i <= len1 and k - i <= len2:
                maxNums1, maxNums2 = maxList(nums1, i), maxList(nums2, k - i)
                answerList.append(merge(maxNums1, maxNums2))
        return max(answerList)
