# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, curr = None, head
        
        while curr:
            nxt = curr.next
            curr.next = prev  #break the link and point it to prev
            prev = curr       #move the prev to curr
            curr = nxt
        return prev
            