class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i,item in enumerate(nums):
            other = target - item
            if other in cache:
                return [i,cache[other]]
            cache[item] = i