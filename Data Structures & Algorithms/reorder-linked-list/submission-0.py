# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        current = head
        while current.next:
            last = head
            previous = head

            temp = current.next

            while last.next:
                last = last.next

            while previous.next is not last:
                previous = previous.next            

            previous.next = None
            current.next = last
            last.next = temp

            current = temp