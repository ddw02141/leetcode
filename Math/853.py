from typing import List

from heapq import heapify, heappop


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # target = position[i] + speed[i] * time[i]
        # time[i] = (target - position[i]) / speed[i]
        numCarFleet = 0
        time = [(target - position[i]) / speed[i] for i in range(len(position))]
        sortedPosition = [(position, i) for i, position in enumerate(position)]
        sortedPosition.sort(reverse=True)
        timeHeap = [(time, i) for i, time in enumerate(time)]
        heapify(timeHeap)
        usedIdx = set()
        for position, idx in sortedPosition:
            if idx in usedIdx:
                continue
            while timeHeap and timeHeap[0][0] <= time[idx]:
                _, timeIdx = heappop(timeHeap)
                usedIdx.add(timeIdx)
            numCarFleet += 1
            usedIdx.add(idx)
        return numCarFleet


if __name__ == "__main__":
    solution = Solution()
    print(solution.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
