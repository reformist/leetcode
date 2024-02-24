# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        node = l1
        val1 = ''
        while node is not None:
            val1 = str(node.val) + val1 # add to the front
            node = node.next
        
        node = l2
        val2 = ''
        while node is not None:
            val2 = str(node.val) + val2 # add to the front
            node = node.next
        
        val1 = int(val1)
        val2 = int(val2)

        total = val1 + val2
        total = str(total)

        # iterate from the front of the string

        # reverse it first
        # maybe put them in a list and then link them after?

        total = total[::-1]
        node_list = []

        for i in range(len(total)):
            v = total[i]

            node = ListNode()
            node.val = v

            node_list.append(node)

        for i in range(len(node_list)):
            node = node_list[i]

            if node == node_list[-1]: # at the last node
                node.next = None
            else:
                node.next = node_list[i+1]
            
        return node_list[0]
