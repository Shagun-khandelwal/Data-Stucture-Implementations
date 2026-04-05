# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # temp = head
        # list_len = 0
        # while temp != None:
        #     list_len += 1
        #     temp = temp.next
        # target = list_len-n # remove element after this element
        # print(target)
        # if list_len==1:
        #     head = head.next
        #     return head
        # temp = head
        # if target == 0 :
        #     head = head.next
        #     return head
        # for _ in range(target-1):
        #     temp = temp.next
        # temp.next = temp.next.next if temp.next !=None else None
        # return head 
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        if not fast: # remove first element
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head