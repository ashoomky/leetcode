# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # reverse linked list 1
        previous1, current1 = None, l1
        while current1:
            temp = current1.next
            current1.next = previous1
            previous1 = current1
            current1 = temp
        
        l1_integer = ""
        while previous1:
            l1_integer += str(previous1.val)
            current1 = previous1
            previous1 = previous1.next

        # reverse linked list 2
        previous2, current2 = None, l2
        while current2:
            temp = current2.next
            current2.next = previous2
            previous2 = current2
            current2 = temp
        
        l2_integer = ""
        while previous2:
            l2_integer += str(previous2.val)
            current2 = previous2
            previous2 = previous2.next

        # add the values and convert back to string
        result = int(l1_integer) + int(l2_integer)
        result = str(result)

        # iterate through string and store in linked list
        dummy = node = ListNode()
   
        for digit in result[::-1]:
            node.next = ListNode(int(digit))
            node = node.next
        return dummy.next
       

        