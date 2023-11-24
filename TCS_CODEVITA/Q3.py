import heapq

def max_time_to_escape(fortress):
    def dijkstra():
        heap = [(0, 0, 0)]  # (distance, row, col)
        distances = {(0, 0): 0}

        while heap:
            dist, row, col = heapq.heappop(heap)

            if row == m - 1 and col == n - 1:
                return dist

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row, new_col = row + dr, col + dc

                if 0 <= new_row < m and 0 <= new_col < n and (new_row, new_col) not in distances and fortress[new_row][new_col] == 0:
                    distances[(new_row, new_col)] = dist + 1
                    heapq.heappush(heap, (dist + 1, new_row, new_col))

        return float('inf')

    m, n = len(fortress), len(fortress[0])
    initial_time = dijkstra()  # Find the initial shortest path without blocking any room

    max_time = 0

    for i in range(m):
        for j in range(n):
            if fortress[i][j] == 0:
                fortress[i][j] = 1  # Block the room temporarily
                max_time = max(max_time, dijkstra())  # Recalculate the path with the blocked room
                fortress[i][j] = 0  # Unblock the room for the next iteration

    return max_time if max_time < float('inf') else -1

# Example usage:
fortress_structure = [
    [0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0]
]

result = max_time_to_escape(fortress_structure)
print(result)
