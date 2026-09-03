class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repeated_elements = set()
        for i in nums:
            if i in repeated_elements:
                return True
            else:
                repeated_elements.add(i)

        return False
                
        