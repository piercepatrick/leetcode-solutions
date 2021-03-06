# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        prev = None
        while (cur != None):
            cur = cur.next
            head.next = prev
            prev = head
            head = cur
        
        return prev
                
        