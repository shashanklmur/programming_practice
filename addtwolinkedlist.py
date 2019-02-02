# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        carry = 0
        head = ListNode(l1.val+l2.val)
        if head.val >= 10:
            head.val %= 10
            carry = 1
        node = head
        l1 = l1.next
        l2 = l2.next
        while l1 and l2:
            node.next = ListNode(l1.val + l2.val + carry)
            node = node.next
            if node.val >= 10:
                node.val %= 10
                carry = 1
            else:
                carry = 0
            l1 = l1.next
            l2 = l2.next
        while l1:
            node.next = ListNode(l1.val+carry)
            if carry:
                carry = 0
            node = node.next
            if node.val >= 10:
                node.val %= 10
                carry = 1
            l1 = l1.next
        while l2:
            node.next = ListNode(l2.val+carry)
            if carry:
                carry = 0
            node = node.next
            if node.val >= 10:
                node.val %= 10
                carry = 1
            l2 = l2.next
        if carry:
            node.next = ListNode(carry)
        
        return head
