class Solution:

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.findMaxRob(nums[1:]), self.findMaxRob(nums[:-1]))

    # bottom-up approach
    def findMaxRob(self, nums: List[int]) -> int:
        nums.append(0)

        for i in range(len(nums) - 3, -1, -1):
            nums[i] = max(nums[i] + nums[i + 2], nums[i + 1])

        return max(nums[0], nums[1])