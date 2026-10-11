# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        curr = prev
        previous = None
        counter = 1

        while curr and counter < n:
            previous = curr
            curr = curr.next
            counter += 1 
        
        if curr:
            if previous:
                previous.next = curr.next
            else:
                prev = curr.next

        curr = prev
        new_head = None

        while curr:
            next_node = curr.next
            curr.next = new_head
            new_head = curr
            curr = next_node

        return new_head