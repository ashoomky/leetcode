# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """

        # finding midpoint (slow pointer)
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        # splitting the two lists by setting slow.next to None
        slow.next = None

        # reversing list
        previous = None
        while second_half:
            temp = second_half.next
            second_half.next = previous
            previous = second_half
            second_half = temp
        
        # merging lists
        first, second = head, previous
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        