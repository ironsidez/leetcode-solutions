from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1current = l1
        while True:
            carry = (l1current.val + l2.val) // 10
            l1current.val = (l1current.val + l2.val) % 10
            if carry:
                if l2.next:
                    l2.next.val += carry
                else:
                    l2.next = ListNode(carry)

            if l2.next:
                l2 = l2.next
                if l1current.next:
                    l1current = l1current.next
                else:
                    l1current.next = ListNode(0)
                    l1current = l1current.next
            else:
                break

        return l1