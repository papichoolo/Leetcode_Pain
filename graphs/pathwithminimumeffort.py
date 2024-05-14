'''

This code implements a solution to find the minimum effort required to travel from the top-left cell to the bottom-right cell in a grid using Dijkstra's algorithm. Here's a breakdown of the code:

The function MinimumEffort takes three parameters: rows and columns, representing the dimensions of the grid, and heights, a 2D list representing the heights of each cell in the grid.

It initializes a priority queue pq with a tuple (0, 0, 0) representing the initial cell (0, 0) with an initial effort of 0. It also initializes a 2D list dist to store the minimum effort required to reach each cell, initialized with infinity for all cells except the top-left cell, which is initialized with 0.

It defines the directions to move: up, down, left, and right, represented by the changes in row (dr) and column (dc) indices.

It enters a loop to perform Dijkstra's algorithm until the priority queue is empty. Inside the loop:

It pops the cell with the minimum effort from the priority queue.
If the popped cell is the bottom-right cell, it returns the effort, indicating the minimum effort required to reach the destination.
It iterates over the four possible directions and calculates the effort required to move to each neighboring cell.
If the calculated effort to reach a neighboring cell is less than the effort stored in dist for that cell, it updates the dist array and adds the cell to the priority queue.
If no path is found (the loop exits without finding the bottom-right cell), it returns 0.
'''

from typing import List


import heapq

class Solution:
    def MinimumEffort(self, rows: int, columns: int, heights: List[List[int]]) -> int:
        pq = [(0, 0, 0)]  # (effort, row, column)
        dist = [[float('inf')] * columns for _ in range(rows)]
        dist[0][0] = 0
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        
        while pq:
            diff, row, col = heapq.heappop(pq)
            
            if row == rows - 1 and col == columns - 1:
                return diff
            
            for i in range(4):
                newr = row + dr[i]
                newc = col + dc[i]
                
                if 0 <= newr < rows and 0 <= newc < columns:
                    neweffort = max(abs(heights[row][col] - heights[newr][newc]), diff)
                    if neweffort < dist[newr][newc]:
                        dist[newr][newc] = neweffort
                        heapq.heappush(pq, (neweffort, newr, newc))
        return 0



