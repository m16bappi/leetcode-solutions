import unittest
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()
        n = len(candidates)

        def combination(curr: int, track: List[int]):
            total = sum(track)
            if total > target:
                return
            if total == target:
                results.append(track[:])
                return

            for i in range(curr, n):
                if i > curr and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    continue
                track.append(candidates[i])
                combination(i + 1, track)
                track.pop()

        combination(0, [])
        return results


class TestCombinationSum2(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_case_1(self):
        self.assertEqual(
            sorted(self.sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)),
            sorted([[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
        )

    def test_case_2(self):
        self.assertEqual(self.sol.combinationSum2([2, 4, 6], 5), [])

    def test_case_3(self):
        self.assertEqual(self.sol.combinationSum2([3, 3, 3, 3], 3), [[3]])

    def test_case_4(self):
        self.assertEqual(
            sorted(self.sol.combinationSum2([1, 2, 2, 3, 4, 5], 5)),
            sorted([[1, 2, 2], [1, 4], [2, 3], [5]]),
        )

    def test_case_5(self):
        self.assertEqual(self.sol.combinationSum2([1, 1, 1, 1], 10), [])

    def test_case_6(self):
        self.assertEqual(
            sorted(self.sol.combinationSum2([2, 5, 2, 1, 2], 5)),
            sorted([[1, 2, 2], [5]]),
        )


if __name__ == "__main__":
    unittest.main()
