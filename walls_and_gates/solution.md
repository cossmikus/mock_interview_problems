```
from typing import List
import collections

class Solution:
    def walls_and_gates(self, rooms: List[List[int]]) -> None:
        if not rooms:
            return
        
        # Dimensions of the grid
        row, col = len(rooms), len(rooms[0])
        
        # Constants for gates and empty rooms
        INF = 2147483647
        GATE = 0
        
        # Queue for BFS
        queue = collections.deque()
        
        # Enqueue all the gates initially
        for r in range(row):
            for c in range(col):
                if rooms[r][c] == GATE:
                    queue.append((r, c))
        
        # Directions for movement (right, left, down, up)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # BFS from the gates
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                # Check if the new cell is within bounds and if it's an empty room
                if 0 <= new_r < row and 0 <= new_c < col and rooms[new_r][new_c] == INF:
                    rooms[new_r][new_c] = rooms[r][c] + 1  # Update distance from the gate
                    queue.append((new_r, new_c))  # Add the cell to the queue for further exploration

```