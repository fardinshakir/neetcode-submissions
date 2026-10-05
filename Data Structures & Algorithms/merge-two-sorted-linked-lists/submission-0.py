# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newlist = ListNode()
        
        newhead = newlist
        head1 = list1
        head2 = list2

        while head1 and head2:
            if head1.val >= head2.val:
                newlist.next = head2
                head2 = head2.next
            elif head1.val < head2.val:
                newlist.next = head1
                head1 = head1.next

            newlist = newlist.next
            
        newlist.next = head1 or head2
        return newhead.next