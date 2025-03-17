import unittest


class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result = []

        def combination(curr: int, track: list[int] = []):
            if len(track) == k:
                if sum(track) == n:
                    result.append(track[:])
                return

            for i in range(curr, 10):
                track.append(i)
                combination(i + 1, track)
                track.pop()

        combination(1)
        return result


class TestCombinationSum3(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_single_combination(self):
        self.assertEqual(self.sol.combinationSum3(3, 7), [[1, 2, 4]])

    def test_multiple_combinations(self):
        self.assertEqual(
            self.sol.combinationSum3(3, 9), [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
        )
        self.assertEqual(self.sol.combinationSum3(4, 10), [[1, 2, 3, 4]])

    def test_no_combination(self):
        self.assertEqual(self.sol.combinationSum3(2, 18), [])

    def test_maximum_value(self):
        self.assertEqual(self.sol.combinationSum3(1, 9), [[9]])

    def test_invalid_case(self):
        self.assertEqual(self.sol.combinationSum3(5, 4), [])


if __name__ == "__main__":
    unittest.main()
