

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        current_profit = price - min_price
        if current_profit > max_profit:
            max_profit = current_profit
    return max_profit
        
prices = [10,1,5,6,7,1]
print(maxProfit(prices))

"""
Input: prices = [10,1,5,6,7,1]
buy on day 2 for 1 dollar

Output: 6

"""
