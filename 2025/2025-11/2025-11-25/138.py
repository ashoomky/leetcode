"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        old_to_copy = {None: None}

        # creating copies of all nodes
        current = head
        while current :
            copy = Node(current.val)
            old_to_copy[current] = copy
            current = current.next
            
        current = head
        while current:
            copy = old_to_copy[current]
            copy.next = old_to_copy[current.next]
            copy.random = old_to_copy[current.random]
            current = current.next
        return old_to_copy[head]

        