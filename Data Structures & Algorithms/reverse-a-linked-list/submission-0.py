# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head

        if (temp == None or temp.next == None):
            return temp

        p = head
        n = head.next
        head.next = None

        while (n.next != None):
            head = n
            n = n.next
            head.next = p
            p = head

        n.next = head
        head = n

        return head

        