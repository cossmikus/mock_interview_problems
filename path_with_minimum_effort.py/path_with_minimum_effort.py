
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
       pass 


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
