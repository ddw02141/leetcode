from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passengers = [0 for _ in range(1000 + 1)]
        for num, start, end in trips:
            passengers[start] += num
            passengers[end] -= num

        passenger = 0
        for i in range(1000 + 1):
            passenger += passengers[i]
            if passenger > capacity:
                return False

        return True
