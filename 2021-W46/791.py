class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_list = [s_sub for s_sub in s]
        order_map = {o_sub: i for i, o_sub in enumerate(order)}
        s_list.sort(key=lambda x: order_map.get(x, -1))
        return "".join(s_list)
