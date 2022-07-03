from typing import List


class Solution:
    def minmax_gas_dist(self, stations: List[int], k: int) -> float:
        """
        k=4: [-26, -21, -18, -8, -5, -4, -4, -3, -2]
        k=3: [-21, -18, -13, -13, -8, -5, -4, -4, -3, -2]
        k=2: [-18, -13, -13, -10.5, -10.5, -8, -5, -4, -4, -3, -2]
        k=1: [-13, -13, -10.5, -10.5, -9, -9, -8, -5, -4, -4, -3, -2]
        k=0: [-13, -10.5, -10.5, -9, -9, -8, -6.5, -6.5, -5, -4, -4, -3, -2]

        binary search!
        """
        distances = []
        for s1, s2 in zip(stations, stations[1:]):
            distances.append(s2 - s1)
        left, right, answer = 0, 10 ** 8, 10 ** 8
        print(self.getDesiredStationCount(10.92, distances))
        print(self.getDesiredStationCount(10.5, distances))
        while left <= right:
            mid = (left + right) / 2
            desiredStationCount = self.getDesiredStationCount(mid, distances)
            if desiredStationCount <= k:
                answer = min(answer, mid)
                right = mid - 1e-6
            else:
                left = mid + 1e-6

        return answer

    def getDesiredStationCount(self, limit, distances):
        return sum(d // limit - 1 if d % limit == 0 else d // limit for d in distances)
