# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res_list = None
        temp = None
        carry = 0
        while l1 != None and l2!= None:
            curr_sum = l1.val + l2.val + carry
            carry = 0
            if curr_sum >=10:
                carry = curr_sum // 10
                curr_sum = curr_sum % 10
            if res_list == None:
                res_list = ListNode(curr_sum)
                temp = res_list
            else:
                temp.next = ListNode(curr_sum)
                temp = temp.next
            l1 = l1.next
            l2 = l2.next
        if l1 != None:
            while l1!=None:
                curr_sum = l1.val + carry
                carry = 0
                if curr_sum >=10:
                    carry = curr_sum // 10
                    curr_sum = curr_sum % 10
                temp.next = ListNode(curr_sum)
                l1 = l1.next
                temp = temp.next
        elif l2!= None:
            while l2!=None:
                curr_sum = l2.val + carry
                carry = 0
                if curr_sum >= 10:
                    carry = curr_sum // 10
                    curr_sum = curr_sum % 10
                temp.next = ListNode(curr_sum)
                l2 = l2.next
                temp = temp.next
        if carry:
            temp.next = ListNode(carry)
        return res_list
