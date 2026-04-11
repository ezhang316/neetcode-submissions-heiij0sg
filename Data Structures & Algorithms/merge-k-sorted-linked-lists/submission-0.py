# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy

        while len(lists) > 0:
            minimum = ListNode(float('inf'))
            min_index = 0
            for index, l in enumerate(lists):
                if l.val < minimum.val:
                    minimum = l
                    min_index = index
            dummy.next = minimum
            dummy = dummy.next
            lists.pop(min_index)
            if minimum.next:
                lists.append(minimum.next)

        return res.next
            