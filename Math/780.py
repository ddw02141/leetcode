class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx > sx and ty > sy:
            tx, ty = tx % ty, ty % tx

        if tx == sx and ty > sy:
            return (ty - sy) % tx == 0
        if ty == sy and tx > sx:
            return (tx - sx) % ty == 0
        return tx == sx and ty == sy
