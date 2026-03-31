# leetcode-101 Symmetry Tree
def isSymmetric(root) -> bool:
    if root.left == None and root.right == None:
        return True
    if root.left == None or root.right == None:
        return False
    que = []
    que.append(root.left)
    que.append(root.right)
    while len(que) > 0:
        first = que.pop(0)
        second = que.pop(0)
        if first == None and second == None:
            continue
        if first == None or second == None:
            return False
        if first.val != second.val:
            return False
        que.append(first.left)
        que.append(second.right)
        que.append(first.right)
        que.append(second.left)
    return True