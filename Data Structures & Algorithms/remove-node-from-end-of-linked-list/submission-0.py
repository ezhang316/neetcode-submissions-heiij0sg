# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # reverse the linked list
        # iterate and remove from the front
        # reverse the list to normal
        # O(3n)

        # can we make it more efficient
        # count list O(n)
        # find position from front: length - n = index to be removed
        # remove without reversing
        # O(2n)

        length = 0
        current = head
        while current != None:
            current = current.next
            length += 1
        
        current = head
        previous = None
        for i in range(length - n):
            print(current.val)
            previous = current
            current = current.next
        
        print(current.val)
        if previous:
            previous.next = current.next
            current = head
        else:
            current = current.next
        
        return current
