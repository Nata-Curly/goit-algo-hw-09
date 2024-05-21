def find_coins_greedy(amount):
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= coin * count
            result[coin] = count

    return result


def find_min_coins(amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    result = dict(sorted(result.items()))
    return result


coins = [50, 25, 10, 5, 2, 1]

print("\nGreedy Algorithm: ", find_coins_greedy(113))
print("\nDynamic Programming Algorithm: ", find_min_coins(113))
