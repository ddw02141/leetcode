def findNumberOfVisibleBuildings(heights):
    """
    :param heights: building heights information as List
    :return: number of visible buildings for each building.
    Every building is looking to the right.
    If one building in its right has same height or bigger height, it cannot see all buildings to the right of that building.
    Buildings are invisible if they are lower than the building on their left.

    [10, 1, 2, 4, 8, 6, 7]
    10: 1 2 4 8 => 4
    1: 2 => 1
    2: 4 => 1
    4: 8 => 1
    8: 6 7 => 2
    6: 7 => 1
    7: 0

    [10, 8, 5, 3, 7, 1]
    10: 8 => 1
    8: 5, 7 => 2
    5: 3, 7 => 2
    3: 7 => 1
    7: 1 => 1
    1: 0

    [5, 4, 3, 2, 1, 2, 3, 4, 5]
    5: 4, 5 => 2
    4: 3, 4 => 2
    3: 2, 3 => 2
    2: 1, 2 => 2
    1: 2 => 1
    2: 3 => 1
    3: 4 => 1
    4: 5 => 1
    5: 0

    find increasing subsequence
    binary search?
    """
    n = len(heights)
    numVisible = [0 for _ in range(n)]
    indicesWithIncreasingHeights = list()
    lastVisibleHeights = [0 for _ in range(n)]
    for i, height in enumerate(heights):
        while indicesWithIncreasingHeights:
            last = indicesWithIncreasingHeights[-1]
            # 나보다 높거나 같은 건물이 나타나면, 그 뒤로는 더 못본다
            if heights[last] <= height:
                numVisible[last] += 1
                indicesWithIncreasingHeights.pop()
                continue
            # 나보다 높거나 같은 건물은 아니면서, 마지막으로 본 건물보다 높으면 볼 수 있다.
            elif lastVisibleHeights[last] < height:
                numVisible[last] += 1
                lastVisibleHeights[last] = height
                break
            else:
                break
        # 자신보다 큰 빌딩이 뒤에 나오면 그 빌딩은 이제 끝난다.
        if i < len(heights) - 1:
            if height <= heights[i + 1]:
                numVisible[i] = 1
            # 만약 나보다 작은 건물이 나왔다면 그 건물보다다 큰 건물이 나올때까지 지켜봐야한다.
            else:  # height > heights[i + 1]
                numVisible[i] += 1
                lastVisibleHeights[i] = heights[i + 1]
                indicesWithIncreasingHeights.append(i)

    return numVisible


if __name__ == '__main__':
    assert findNumberOfVisibleBuildings([10, 1, 2, 4, 8, 6, 7]) == [4, 1, 1, 1, 2, 1, 0]
    assert findNumberOfVisibleBuildings([10, 8, 5, 3, 7, 1]) == [1, 2, 2, 1, 1, 0]
    assert findNumberOfVisibleBuildings([5, 4, 3, 2, 1, 10]) == [2, 2, 2, 2, 1, 0]
    assert findNumberOfVisibleBuildings([5, 4, 3, 2, 1, 2, 3, 4, 5]) == [2, 2, 2, 2, 1, 1, 1, 1, 0]
