# Solution Approach: Combination Sum III

## Problem Statement
Given two integers `k` and `n`, we need to find all possible combinations of `k` distinct numbers from `1` to `9` that sum up to `n`. Each combination should be unique, and numbers must be used only once.

---

## Approach
We use **backtracking** to explore all possible combinations.

### **Step 1: Define Recursive Backtracking Function**
- Use a helper function `combination(curr, track)` where:
  - `curr` represents the starting number (to ensure uniqueness and avoid duplicates).
  - `track` is a list maintaining the current combination being explored.
- Maintain a global `result` list to store valid combinations.

### **Step 2: Base Case**
- If `len(track) == k` (we have selected `k` numbers):
  - Check if `sum(track) == n`.
  - If true, append a copy of `track` to `result`.
  - Return to backtrack.

### **Step 3: Recursive Exploration**
- Iterate `i` from `curr` to `9` (ensuring numbers are used only once and in increasing order).
- **Choose:** Add `i` to `track`.
- **Explore:** Call `combination(i + 1, track)` to continue searching.
- **Unchoose:** Remove `i` (backtrack) to explore other possibilities.

---

## Complexity Analysis
- The worst-case scenario explores all subsets of `{1,2,...,9}`, leading to **O(2⁹) ≈ O(512)** calls.
- However, pruning (ensuring `k` elements and sum `n`) reduces the space significantly.
- Time Complexity: **O(9Ck) ≈ O(9!)** in the worst case.
- Space Complexity: **O(k)** for the recursive call stack.

---

## Example Walkthrough
**Input:** `k = 3, n = 7`

| Step | Track List | Remaining Sum | Action |
|------|-----------|---------------|--------|
| 1 | `[]` | `7` | Start with `1` |
| 2 | `[1]` | `6` | Add `2` |
| 3 | `[1,2]` | `4` | Add `4` (valid) |
| 4 | `[1,2,4]` | `0` | Add to `result`, backtrack |
| 5 | `[1,2]` | `4` | Try next numbers, backtrack |
| 6 | `[1]` | `6` | Try `3`, `5`, etc. |

**Output:** `[[1,2,4]]`

---

## Edge Cases Considered
- `k > 9` (impossible case, return `[]`).
- `n` too large (e.g., `k=3, n=30` → return `[]`).
- `n < k` (not enough numbers to sum up, return `[]`).
- Single number case (e.g., `k=1, n=9` → `[[9]]`).

---

## Conclusion
- **Backtracking** is an effective approach since it systematically explores valid subsets and eliminates unnecessary branches.
- We ensure efficiency by using constraints (`k`, `n`, `curr`) to prune the search space.
- This solution is optimal for small constraints (`1 ≤ k ≤ 9`).