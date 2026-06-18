# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next: return None
        c = 0
        fast  = head
        slow = head
        while c < n:
            c +=1
            fast = fast.next
            if fast is None:
                return head.next
        
        while fast and fast.next:
            fast= fast.next
            slow = slow.next
        slow.next=slow.next.next
        return head