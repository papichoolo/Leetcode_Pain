class Solution:
    def verticalSum(self, root):
        if not root:
            return []

        # Hash map to store the vertical sums
        vertical_sums = {}

        # Helper function to traverse the tree and calculate vertical sums
        def calculate_vertical_sum(node, distance):
            if not node:
                return
            # Update the sum for the current horizontal distance
            if distance in vertical_sums:
                vertical_sums[distance] += node.data
            else:
                vertical_sums[distance] = node.data

            # Traverse left and right subtrees with updated horizontal distances
            calculate_vertical_sum(node.left, distance - 1)
            calculate_vertical_sum(node.right, distance + 1)

        # Start the traversal from the root with a horizontal distance of 0
        calculate_vertical_sum(root, 0)

        # Sort the keys of the hash map to return the vertical sums in left to right order
        sorted_keys = sorted(vertical_sums.keys())

        # Return the vertical sums in the sorted order
        return [vertical_sums[key] for key in sorted_keys]