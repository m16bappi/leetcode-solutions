# 2024. Maximize confusion of the exam
# we are going to apply window sliding approach for solve this problem
# here k is fixed but we need to calculate dynamic slide for count the T
# Test cases: TTFTTFTT, output: 5

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        counter = 0
        true_left = 0
        false_left = 0
        false_k = k
        true_k = k
        for right in range(len(answerKey)):
            if answerKey[right] == "F":
                false_k -= 1

            if answerKey[right] == "T":
                true_k -= 1

            while false_k < 0:
                if answerKey[false_left] == "F":
                    false_k += 1
                false_left += 1

            while true_k < 0:
                if answerKey[true_left] == "T":
                    true_k += 1
                true_left += 1
            counter = max(counter, (right - false_left + 1), (right - true_left + 1))
        return counter
