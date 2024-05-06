
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def noSiblingUtil(root, siblings):
    if root is None:
        return

    # If the current node has no left or right child, check if it has a sibling
    if root.left is None and root.right is None:
        return

    # If the current node has only one child, add the sibling to the list
    if root.left is not None and root.right is None:
        siblings.append(root.left.data)
    elif root.right is not None and root.left is None:
        siblings.append(root.right.data)

    # Recursively traverse the left and right subtrees
    noSiblingUtil(root.left, siblings)
    noSiblingUtil(root.right, siblings)

def noSibling(root):
    siblings = []
    noSiblingUtil(root, siblings)
    if not siblings:
        return [-1]  # If all nodes have a sibling, return [-1]
    else:
        siblings.sort()  # Sort the list of nodes without siblings
        return siblings