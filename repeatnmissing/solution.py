class Solution:
    def findTwoElement(self, arr, n):
        visited = set()
        repeated = 0
        total_sum = 0
        actual_sum = (n * (n + 1)) // 2  # Sum of first n natural numbers

        for num in arr:
            if num in visited:
                repeated = num
            visited.add(num)
            total_sum += num

        missing = actual_sum - (total_sum - repeated)

        return [repeated, missing]
        # code here

