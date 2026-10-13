class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        day = 0
        lowest_so_far = prices[0]
        best_so_far = 0
        while day < len(prices):
            profit = prices[day] - lowest_so_far
            if lowest_so_far > prices[day]:
                lowest_so_far = prices[day]

            if profit > best_so_far:
                best_so_far = profit
            day += 1
        return best_so_far
        