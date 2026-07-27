class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1<=nums[i]<=n and nums[nums[i]-1] != nums[i]:#这里一定是while而不是if，因为交换后nums[i]可能也在1-n的范围内，所以也需要交换，如果只交换一次，那么这个nums[i]可能就会被忽略
                j = nums[i] - 1
                nums[i],nums[j] = nums[j],nums[i]
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n + 1
