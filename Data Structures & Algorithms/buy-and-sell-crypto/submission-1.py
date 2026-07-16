class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_sell = len(prices) - 1
        res = 0

        while (current_sell > 0):
            temp = current_sell - 1
            price = 0
            while (prices[temp] < prices[current_sell]):
                price = prices[current_sell] - prices[temp]
                temp -= 1
                res = max(price, res)
                if (temp < 0):
                    return res
            current_sell = temp

        return res
       