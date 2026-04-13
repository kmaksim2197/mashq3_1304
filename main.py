class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root):
    if not root:
        return 0
    return 1 + max(solve(root.left), solve(root.right))

root = Node(1, Node(2, Node(4)), Node(3))
print(solve(root))
