import unittest
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        v = defaultdict(list)
        for idx, w in enumerate(strs, start=1):
            s_w = "".join(sorted(w))
            v[s_w].append(w)
        return list(v.values())


class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case_1(self):
        self.assertListEqual(
            self.sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        )

    def test_case_2(self):
        self.assertEqual(self.sol.groupAnagrams(["a"]), [["a"]])


if __name__ == "__main__":
    unittest.main()
