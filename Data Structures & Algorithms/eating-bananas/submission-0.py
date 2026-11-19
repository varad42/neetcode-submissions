class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        best = max(piles)
        high = max(piles)

        while low <= high:
            mid = (low + high) // 2
            total_hours = 0

            for pile in piles:
                required_hour = (pile + mid - 1) // mid
                total_hours += required_hour

            if total_hours > h:
                low = mid + 1
            else:
                best = mid          
                high = mid - 1

        return best
        