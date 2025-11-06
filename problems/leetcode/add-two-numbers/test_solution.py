import unittest
from typing import Optional
from .solution import Solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TestAddTwoNumbers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def list_to_linkedlist(self, lst):
        if not lst:
            return None
        head = ListNode(lst[0])
        current = head
        for val in lst[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    def linkedlist_to_list(self, head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    def test_example_case(self):
        l1 = self.list_to_linkedlist([2, 4, 3])
        l2 = self.list_to_linkedlist([5, 6, 4])
        result = self.solution.addTwoNumbers(l1, l2)
        expected = [7, 0, 8]
        self.assertEqual(self.linkedlist_to_list(result), expected)
    
    def test_single_digit(self):
        l1 = self.list_to_linkedlist([2])
        l2 = self.list_to_linkedlist([5])
        result = self.solution.addTwoNumbers(l1, l2)
        expected = [7]
        self.assertEqual(self.linkedlist_to_list(result), expected)
    
    def test_different_lengths(self):
        l1 = self.list_to_linkedlist([9, 9])
        l2 = self.list_to_linkedlist([1])
        result = self.solution.addTwoNumbers(l1, l2)
        expected = [0, 0, 1]
        self.assertEqual(self.linkedlist_to_list(result), expected)
    
    def test_carry_over(self):
        l1 = self.list_to_linkedlist([9, 9, 9])
        l2 = self.list_to_linkedlist([1])
        result = self.solution.addTwoNumbers(l1, l2)
        expected = [0, 0, 0, 1]
        self.assertEqual(self.linkedlist_to_list(result), expected)

if __name__ == '__main__':
    unittest.main()