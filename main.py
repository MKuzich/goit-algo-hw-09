coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
    res = {}
    for coin in coins:
        selected_coins = amount // coin
        if selected_coins > 0:
            res[coin] = selected_coins
            amount = amount % coin
    return res

def find_min_coins(amount):
    dp = [0] + [float('inf')] * amount
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    res = {}
    i = amount
    while i > 0:
        for coin in coins:
            if i - coin >= 0 and dp[i] == dp[i - coin] + 1:
                res[coin] = res.get(coin, 0) + 1
                i -= coin
                break
    return res

print('Greedy Algorithm:')
print(find_coins_greedy(113))
print('Dynamic Programming Algorithm:')
print(find_min_coins(113))