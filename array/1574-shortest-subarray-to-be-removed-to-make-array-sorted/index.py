from typing import List


class Solution:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        arr.append(float("inf"))
        arr.insert(0, 0)

        left, right = 0, len(arr) - 1
        shortest = float("inf")

        while left < len(arr) - 2 and arr[left] <= arr[left + 1]:
            left += 1

        while left >= 0:
            while right - 1 > left and arr[
                    right - 1] >= arr[left] and arr[right] >= arr[right - 1]:
                right -= 1

            shortest = min(shortest, right - left - 1)
            left -= 1

        return shortest