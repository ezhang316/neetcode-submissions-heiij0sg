# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:       
        
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        previous = slow.next = None
        while second_half:
            temp = second_half.next
            second_half.next = previous
            previous = second_half
            second_half = temp

        first_half = head
        second_half = previous

        while second_half:
            fh_next = first_half.next
            sh_next = second_half.next

            first_half.next = second_half
            second_half.next = fh_next

            first_half = fh_next
            second_half = sh_next
        

