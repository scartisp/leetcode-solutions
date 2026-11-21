# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        fast = slow = behindSlow = head
        if fast.next is None:
            return None

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            behindSlow = slow
            slow = slow.next
        
        behindSlow.next = slow.next
        return head
