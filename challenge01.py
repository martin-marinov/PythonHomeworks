COINS = (100, 50, 20, 10, 5, 2, 1)


def calculate_coins(coins):
    result = {}
    coins *= 100
    for coin in COINS:
        result[coin] = coins//coin
        coins %= coin
    return result
