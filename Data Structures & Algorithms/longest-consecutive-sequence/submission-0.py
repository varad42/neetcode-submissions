class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            if len(nums) == 0:
                return 0

            nums = sorted(nums)
            current = 1
            best = 1

            for i in range(len(nums) - 1):
                if nums[i] + 1 == nums[i+1]:
                    current = current + 1

                    if current > best:
                        best = current

                elif nums[i] == nums[i+1]:
                    continue
                else:
                    current = 1

            return best
        