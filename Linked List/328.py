# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        secondNode = head.next
        oddLastNode = None
        d = dict()
        cur = head
        idx = 1
        while cur:
            if idx % 2 == 1:
                oddLastNode = cur
            idx += 1
            if cur.next:
                d[cur] = cur.next.next
            cur = cur.next

        cur = head
        while cur:
            if cur == oddLastNode:
                oddLastNode.next = secondNode
                break
            nextCur = cur.next
            cur.next = d[cur]
            cur = nextCur

        return head
