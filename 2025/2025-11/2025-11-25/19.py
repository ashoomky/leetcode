# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        # retrieving length of linked list
        previous, current = None, head
        length = 0
        while current:
            length += 1
            previous = current
            current = current.next
        
        if length == 1:
            return None 

        # removing nth node
        remove = length - n
        previous, current = None, head

        while remove > 0:
            previous = current
            current = current.next
            remove -= 1

        if previous == None:
            temp = current.next
            current.next = None
            return temp
        
        # attaches everything
        previous.next = current.next

        return head