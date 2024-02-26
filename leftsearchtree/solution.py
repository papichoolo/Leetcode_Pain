'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

def LeftView(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        # Add the first node of each level to the result list
        result.append(queue[0].data)

        # Iterate through the current level and add the non-empty left child of each node to the queue
        for i in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return 

#Driver code