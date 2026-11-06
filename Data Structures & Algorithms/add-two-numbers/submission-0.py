# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        cur1, cur2 = l1, l2
        res = l1
        carry = 0
        while cur1 and cur2:
            sum = cur1.val + cur2.val + carry
            carry = 0
            if sum >= 10:
                sum -= 10
                carry = 1

            prev = cur1
            prev.val = sum
            cur1 = cur1.next
            cur2 = cur2.next
        
        while cur1 and not cur2:
            sum = cur1.val + carry
            carry = 0
            if sum >= 10:
                sum -= 10
                carry = 1

            prev = cur1
            prev.val = sum
            cur1 = cur1.next

        while cur2 and not cur1:
            sum = cur2.val + carry
            carry = 0
            if sum >= 10:
                sum -= 10
                carry = 1

            prev = cur2
            prev.val = sum
            cur2 = cur2.next

        if carry:
            prev.next = ListNode(carry, None)
            
        return res







