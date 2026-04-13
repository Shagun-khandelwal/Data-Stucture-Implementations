# LeetCode-83. Remove duplicates from sorted linked list

class ListNode:
    def __init__(self,data):
        self.val = data
        self.next = None
    def printlist(self):
        temp = self
        while temp!=None:
            print(temp.val,end=" ")
            temp = temp.next
        print()

def deleteDuplicates(head: [ListNode]) -> [ListNode]:
    temp = head
    while temp != None:
        if temp.next != None:
            while temp.next.val == temp.val:
                temp.next = temp.next.next
                if temp.next == None:
                    break
        temp = temp.next
    return head

obj = ListNode(1)
obj.next = ListNode(1)
obj.next.next = ListNode(2)

deleteDuplicates(obj)
obj.printlist()