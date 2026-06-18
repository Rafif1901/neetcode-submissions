# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next: return None
        c = 0
        curr = head
        while curr:
            c+=1
            curr = curr.next
        if c == n:
            return head.next
        
        step = 0
        curr = head
        while step < c - n-1:
            step +=1
            curr = curr.next
        curr.next = curr.next.next
        return head