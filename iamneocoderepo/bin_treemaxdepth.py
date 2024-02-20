class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def max_depth(node):
    if node is None:
        return 0
    else:
        left_depth = max_depth(node.left)
        right_depth = max_depth(node.right)
        return max(left_depth, right_depth) + 1

def new_node(data):
    return Node(data)

if __name__ == "__main__":
    root = new_node(1)
    root.left = new_node(2)
    root.right = new_node(3)
    root.left.left = new_node(4)
    print(max_depth(root))
