'''
Example 1: Given list of inputs seperated by space,
properties_prices_per_day = 10 7 5 8 11 9
The code should return 6 (buying for 5 and selling for 11).
As You can buy a property on day 3 and can sell it on day 5 to get the maximum possible returns.
Example 2: Given list of inputs seperated by space,
properties_prices_per_day = 20 9 8 11 4
The code should return 3 (buying for 8 and selling for 11).
As You can buy property on day 3 and sell it on day 4 to get maximum returns.
If there is no profit that can be made then output -1.
'''


# def get_max_profit(prices):
#     buy_val = prices[0]
#     sell_val = prices[-1]
#     for i, x in enumerate(prices):
#         if x<min_val and x.index < sell_val.index:
#             min_val = x
#         elif x> max_val:
#             max_val = x
            
#     max_profit = max_val-min_val
#     if max_profit == 0:
#         max_profit = -1
#     else:
#         max_profit
    
#     return max_profit

def get_max_profit(nums):
    max_profit = 0
    buy = nums[0]
    sell = nums[0]
    for i, cur in enumerate(nums):
        if cur < buy:
            buy = cur
        elif cur > buy:
            profit = cur - buy
            if profit > max_profit:
                max_profit = profit


    max_profit = -1 if max_profit == 0 else max_profit


if __name__=='__main__':
    prices = list(map(int, input().split(' ')))
    print(get_max_profit(prices))