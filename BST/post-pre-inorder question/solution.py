class Solution:
    def buildTree(self, inorder, postorder, n):
        if n == 0:
            return None
        
        root_val = postorder[n - 1]
        root = Node(root_val)
        
        root_index = inorder.index(root_val)
        
        root.right = self.buildTree(inorder[root_index + 1:], postorder[root_index:n - 1], n - root_index - 1)
        root.left = self.buildTree(inorder[0:root_index], postorder[0:root_index], root_index)
        
        return root

