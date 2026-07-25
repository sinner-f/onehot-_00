class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i,item in enumerate(nums):
            other = target - item
            if other in cache:#other匹配cache的键而不是值
                return [i,cache[other]]
            cache[item] = i