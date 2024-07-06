class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
tree3 = TreeNode(1, TreeNode(2), None)

print(isSameTree(tree1, tree2))  # should return True
print(isSameTree(tree1, tree3))  # should return False
