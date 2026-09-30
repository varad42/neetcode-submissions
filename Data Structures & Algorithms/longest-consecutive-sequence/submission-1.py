class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            if len(nums) == 0:
                return 0

            num_set = set(nums)
            best = 0

            for x in num_set:

                if (x - 1) in num_set:
                    continue

                length = 1

                while (x + length) in num_set:
                    length += 1

                if length > best:
                    best = length

            return best
        
        