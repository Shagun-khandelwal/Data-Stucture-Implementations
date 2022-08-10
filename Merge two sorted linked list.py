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
def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    merged = ListNode(-999)
    add = merged
    i = list1
    j = list2
    while i != None or j != None:
        if i == None:
            break
        if j == None:
            break
        if i.val <= j.val:
            newnode = ListNode(i.val)
            add.next = newnode
            add = add.next
            i = i.next
        else:
            newnode = ListNode(j.val)
            add.next = newnode
            add = add.next
            j = j.next
    if i:
        while i != None:
            newnode = ListNode(i.val)
            add.next = newnode
            add = add.next
            i = i.next
    if j:
        while j != None:
            newnode = ListNode(j.val)
            add.next = newnode
            add = add.next
            j = j.next
    merged = merged.next
    return merged
# next 6 line is just for taking inputs ignore them i make them in hurry
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# list1.printlist()
# list2.printlist()

merged_list = mergeTwoLists(list1,list2)
merged_list.printlist()