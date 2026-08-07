class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        merged = a + b
        merged.sort()

        s = len(merged)
        k = (s - 1) // 2
        return merged[k] if s % 2 else (merged[k] + merged[k + 1]) / 2

