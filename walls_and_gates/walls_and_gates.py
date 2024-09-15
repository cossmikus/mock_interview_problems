import collections
from typing import (
    List
)
import unittest

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        """
        This method modifies the input 2D grid (rooms) in-place,
        filling each empty room (INF) with the distance to its nearest gate.
        If a room cannot reach any gate, it should remain as INF.
        """
        # write your code here



class TestWallsAndGates(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        rooms = [
            [2147483647, -1, 0, 2147483647],
            [2147483647, 2147483647, 2147483647, -1],
            [2147483647, -1, 2147483647, -1],
            [0, -1, 2147483647, 2147483647]
        ]
        expected_output = [
            [3, -1, 0, 1],
            [2, 2, 1, -1],
            [1, -1, 2, -1],
            [0, -1, 3, 4]
        ]
        self.solution.walls_and_gates(rooms)
        self.assertEqual(rooms, expected_output)

    def test_example_2(self):
        rooms = [
            [0, -1],
            [2147483647, 2147483647]
        ]
        expected_output = [
            [0, -1],
            [1, 2]
        ]
        self.solution.walls_and_gates(rooms)
        self.assertEqual(rooms, expected_output)

    def test_no_gate(self):
        rooms = [
            [-1, -1],
            [2147483647, 2147483647]
        ]
        expected_output = [
            [-1, -1],
            [2147483647, 2147483647]
        ]
        self.solution.walls_and_gates(rooms)
        self.assertEqual(rooms, expected_output)

    def test_all_walls(self):
        rooms = [
            [-1, -1],
            [-1, -1]
        ]
        expected_output = [
            [-1, -1],
            [-1, -1]
        ]
        self.solution.walls_and_gates(rooms)
        self.assertEqual(rooms, expected_output)


if __name__ == '__main__':
    unittest.main()
