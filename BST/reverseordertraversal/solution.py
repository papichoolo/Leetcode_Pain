from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def reverseLevelOrder(root):
    if not root:
        return []

    # Queue for level order traversal
    queue = deque()
    queue.append(root)

    # List to store the reverse level order traversal
    reverse_traversal = []

    while queue:
        level_size = len(queue)
        level_nodes = []

        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Insert the level nodes at the beginning of the traversal list
        reverse_traversal = level_nodes + reverse_traversal

    return reverse_traversal

# Example usage:
# Create the binary tree
root = Node(1)
root.left = Node(3)
root.right = Node(2)

# Print the reverse level order traversal
print(reverseLevelOrder(root))  # Output: [3, 2, 1]
