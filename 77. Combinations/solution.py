import unittest


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []

        def dfs(curr: int, arr: list[int] = []):
            if len(arr) == k:
                result.append(arr)
                return

            for i in range(curr, n + 1):
                arr.append(i)
                dfs(i + 1, arr[:])
                arr.pop()

        dfs(1)
        return result


class TestCombination(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case_1(self):
        self.assertEqual(
            self.sol.combine(n=4, k=2),
            [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]],
        )

    def test_case_2(self):
        self.assertEqual(self.sol.combine(1, 1), [[1]])


if __name__ == "__main__":
    unittest.main()
