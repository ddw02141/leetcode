from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lmax, rmax = -1, -1
        answer = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] > lmax:
                    lmax = height[l]
                else:
                    answer += lmax - height[l]
                l += 1
            else:
                if height[r] > rmax:
                    rmax = height[r]
                else:
                    answer += rmax - height[r]
                r -= 1
        return answer


"""
Solution at 2022-04-27
[0,1,0,2,1,0,1,3,2,1,2,1]
 l                     r
   l
     l                    -> l1 r1 +1
       l
                     r
         l                -> l2 r2 +1
           l              -> l2 r2 +2
             l            -> l2 r2 +1
               l   r      -> l3 r2 +1
               l r        
[0,1,0,2,1,0,1,3,2,1,4,1]
 l                     r
   l
     l                    -> l1 r1 +1
       l
                     r
         l                -> l2 r4 +1
           l              -> l2 r4 +2
             l            -> l2 r4 +1
               l
                 l        -> l3 r4 +1
                   l      -> l3 r4 +2
"""


class Solution2:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        lMax, rMax, minOfMaxes = 0, 0, 0
        answer = 0
        while left < right:
            lh, rh = height[left], height[right]
            lMax = max(lMax, height[left])
            rMax = max(rMax, height[right])
            minOfMaxes = min(lMax, rMax)
            if lh <= rh:
                answer += (minOfMaxes - lh)
                left += 1
            else:
                answer += (minOfMaxes - rh)
                right -= 1
        return answer


if __name__ == "__main__":
    solution = Solution()
    print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
