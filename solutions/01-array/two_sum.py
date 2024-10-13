class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # for idx, num in enumerate(nums): # O(n)
        #     for idx2, num2 in enumerate(nums[idx + 1:], start=idx + 1): # O(n) => o(n^2)
        #         if num + num2 == target:
        #             return (idx, idx2)

        # mapping = {num: idx for idx, num in enumerate(nums)}
        # for idx, num in enumerate(nums): # O(n)
        #     num2 = target - num
        #     idx2 = mapping[num2]
        #     if idx != idx2:
        #         return (idx, idx2)

        mapping = {}
        for idx, num in enumerate(nums):
            num2 = target - num
            if num2 in mapping:
                idx2 = mapping[num2]
                return (idx, idx2)
            mapping[num] = idx
