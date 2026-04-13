# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res_list = None
        temp_i,temp_j = list1,list2
        while temp_i != None and temp_j != None:
            if temp_i.val < temp_j.val:
                if res_list == None:
                    res_list = ListNode(temp_i.val)
                    temp_res_list = res_list
                else:
                    temp_res_list.next = ListNode(temp_i.val)
                    temp_res_list = temp_res_list.next
                temp_i = temp_i.next
            else:
                if res_list == None:
                    res_list = ListNode(temp_j.val)
                    temp_res_list = res_list
                else:
                    temp_res_list.next = ListNode(temp_j.val)
                    temp_res_list = temp_res_list.next
                temp_j = temp_j.next
        while temp_i:
            if res_list == None:
                res_list = ListNode(temp_i.val)
                temp_res_list = res_list
            else:
                temp_res_list.next = ListNode(temp_i.val)
                temp_res_list = temp_res_list.next
            temp_i = temp_i.next
        while temp_j:
            if res_list == None:
                res_list = ListNode(temp_j.val)
                temp_res_list = res_list
            else:
                temp_res_list.next = ListNode(temp_j.val)
                temp_res_list = temp_res_list.next
            temp_j = temp_j.next
        return res_list

