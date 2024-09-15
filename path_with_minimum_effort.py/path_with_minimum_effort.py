
from typing import List
import unittest
import heapq

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


# Testing framework using unittest
class TestMinimumEffortPath(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
        expected_output = 2
        self.assertEqual(self.solution.minimumEffortPath(heights), expected_output)

    def test_example_2(self):
        heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
        expected_output = 1
        self.assertEqual(self.solution.minimumEffortPath(heights), expected_output)

    def test_example_3(self):
        heights = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
        expected_output = 0
        self.assertEqual(self.solution.minimumEffortPath(heights), expected_output)

    def test_single_cell(self):
        heights = [[1]]
        expected_output = 0
        self.assertEqual(self.solution.minimumEffortPath(heights), expected_output)

    def test_increasing_heights(self):
        heights = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_output = 1
        self.assertEqual(self.solution.minimumEffortPath(heights), expected_output)


if __name__ == '__main__':
    unittest.main()
