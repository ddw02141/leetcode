class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        diffs = [b - a for a, b in zip(nums, nums[1:])]
        print(diffs)
        answers = []
        sameCounts = 1
        diff = diffs[0]
        for d in diffs[1:]:
            if d == diff:
                sameCounts += 1
            else:
                if sameCounts >= 2:
                    answers.append(sameCounts)
                sameCounts = 1
                diff = d
        if sameCounts >= 2:
            answers.append(sameCounts)
        numSubArrays = [answer * (answer - 1) // 2 for answer in answers]
        return sum(numSubArrays)
