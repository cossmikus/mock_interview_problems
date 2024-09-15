
```
class Solution:


    """
    @param heights: 2D list of heights
    @return: The minimum effort required to travel from top-left to bottom-right
    """
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # write your code here
        
        rows, cols = len(heights), len(heights[0])
        efforts = [[float('inf')] * cols for _ in range(rows)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        min_heap = [(0, 0, 0)]  # (effort, row, col)
        efforts[0][0] = 0
        
        while min_heap:
            current_effort, x, y = heapq.heappop(min_heap)
            
            if x == rows - 1 and y == cols - 1:
                return current_effort
            
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                
                if 0 <= new_x < rows and 0 <= new_y < cols:
                    effort_needed = max(current_effort, abs(heights[new_x][new_y] - heights[x][y]))
                    
                    if effort_needed < efforts[new_x][new_y]:
                        efforts[new_x][new_y] = effort_needed
                        heapq.heappush(min_heap, (effort_needed, new_x, new_y))
        
        return 0
```