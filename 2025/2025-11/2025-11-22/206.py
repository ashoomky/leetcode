# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
      
        previous, current = None, head
        while current:
            # saving the next node to set current to
            next = current.next
            #setting the pointer to the previous node to reverse
            current.next = previous
            # incrementing our previous node to the next node
            previous = current
            # incrementing the current node to the next node
            current = next
        return previous