from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        times = [0 for _ in range(len(logs))]
        funcIndices = [-1 for _ in range(len(logs))]
        stack = list()
        for idx, log in enumerate(logs):
            funcId, wildCard, timestamp = log.split(":")
            funcId, timestamp = int(funcId), int(timestamp)
            funcIndices[idx] = funcId
            if wildCard == "start":
                stack.append((funcId, idx, timestamp))
            else:
                assert stack
                curFuncId, curIdx, curTimestamp = stack[-1]
                assert curFuncId == funcId
                timeSpend = timestamp - curTimestamp + 1
                times[curIdx] += timeSpend
                stack.pop(-1)
                for _, prevIdx, _ in stack:
                    times[prevIdx] -= times[curIdx]
        answer = [0 for _ in range(n)]
        for idx, time in enumerate(times):
            answer[funcIndices[idx]] += time
        return answer


if __name__ == "__main__":
    solution = Solution()

    print("------------------ Test Case 1 ------------------")
    sol = solution.exclusiveTime(1, ["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"])
    ans = [8]
    assert ans == sol, f"Expected {ans} Actual {sol}"
    print("------------------ Test Case 2 ------------------")
    sol = solution.exclusiveTime(1, ["0:start:0", "0:start:1", "0:start:2", "0:end:3", "0:end:4", "0:end:5"])
    ans = [6]
    assert ans == sol, f"Expected {ans} Actual {sol}"
    print("------------------ Test Case 3 ------------------")
    sol = solution.exclusiveTime(8, ["0:start:0",
                                     "1:start:5",
                                     "2:start:6",
                                     "3:start:9",
                                     "4:start:11",
                                     "5:start:12",
                                     "6:start:14",
                                     "7:start:15",
                                     "1:start:24",
                                     "1:end:29",
                                     "7:end:34",
                                     "6:end:37",
                                     "5:end:39",
                                     "4:end:40",
                                     "3:end:45",
                                     "0:start:49",
                                     "0:end:54",
                                     "5:start:55",
                                     "5:end:59",
                                     "4:start:63",
                                     "4:end:66",
                                     "2:start:69",
                                     "2:end:70",
                                     "2:start:74",
                                     "6:start:78",
                                     "0:start:79",
                                     "0:end:80",
                                     "6:end:85",
                                     "1:start:89",
                                     "1:end:93",
                                     "2:end:96",
                                     "2:end:100",
                                     "1:end:102",
                                     "2:start:105",
                                     "2:end:109",
                                     "0:end:114"])
    ans = [20, 14, 35, 7, 6, 9, 10, 14]
    assert ans == sol, f"Expected {ans} Actual {sol}"
