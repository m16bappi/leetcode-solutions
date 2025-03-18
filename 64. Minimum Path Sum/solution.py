import unittest


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]

        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]


class TestMinimumPathSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case_1(self):
        self.assertEqual(self.sol.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]), 7)

    def test_case_2(self):
        self.assertEqual(self.sol.minPathSum([[1, 2, 3], [4, 5, 6]]), 12)


if __name__ == "__main__":
    unittest.main()
