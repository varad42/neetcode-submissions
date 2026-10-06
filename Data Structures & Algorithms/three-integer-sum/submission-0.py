class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue                          # dedupe the fixed number

            target = -nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[left] + nums[right]

                if total == target:
                    result.append([nums[i],         nums[left], nums[right]])  # triplet of VALUES

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1                 # dedupe the left walker

                elif total > target:
                    right -= 1
                else:
                    left += 1

        return result