# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #If list contains no nodes or only two nodes
        if not head or not head.next:
            return head

        odd_head = odd = head
        even_head = even = head.next

        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next

        odd.next = even_head

        return odd_head