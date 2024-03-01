class Solution:
    def findExtra(self, a, b, n):
        return next((i for i, (x, y) in enumerate(zip(a, b)) if x != y), n-1)