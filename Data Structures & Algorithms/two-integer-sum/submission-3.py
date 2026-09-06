class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, value in enumerate(nums):
            num2 = target - value

            if num2 in seen:
                return [seen[num2], i]

            seen[value] = i