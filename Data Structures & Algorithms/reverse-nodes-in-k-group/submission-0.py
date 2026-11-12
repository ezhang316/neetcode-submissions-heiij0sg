# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        length = 0
        dummy = head
        while dummy:
            length += 1
            dummy = dummy.next
        num_partitions = length // k
        heads, tails = [None] * num_partitions, [None] * num_partitions
        cur = head
        for i in range(num_partitions):
            tails[i] = cur
            prev = None
            for _ in range(k):
                tmp = cur
                cur = cur.next
                tmp.next = prev
                prev = tmp
            heads[i] = prev

        for i in range(num_partitions - 1):
            tails[i].next = heads[i + 1]
        
        tails[num_partitions - 1].next = cur

        return heads[0]
        

