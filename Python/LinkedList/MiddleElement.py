# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        start = end = head
        while start and start.next:
            start=start.next.next
            end=end.next
        return end