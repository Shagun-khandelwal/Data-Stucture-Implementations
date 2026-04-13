# LeetCode-141. Linked List Cycle

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


def hasCycle(head: [ListNode]) -> bool:
    number=-9988
    repeat=False
    temp=head
    while temp!=None:
        if temp.val!=number:
            temp.val = number
            temp = temp.next
        else:
            repeat = True
            break
    return repeat

obj = ListNode(4)
obj.next = r = ListNode(0)
obj.next.next = ListNode(2)
obj.next.next.next = r

print(hasCycle(obj))