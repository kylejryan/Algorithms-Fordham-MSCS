# Kyle Ryan
# CISC 5825 Computer Algorithms
# Professor Josephine Altzman

# Function Intakes Coins Denomination and Target Amount
def coinChange(coins, amount):

    # Initializing Array for All Values to be Inf
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    # Iterates Through Coins Denomination
    for coin in coins:
        # Looks for the Minimum 
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Returns True if Change Can be Made, False if Change Cannot be Made
    return dp[amount] != float('inf')


# Function Intakes Coins Denomination, Target Amount, and Coin Limit
def coinChangeLimit(coins, amount, limit):

    # Initializing Array for All Values to be Inf
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    # Iterates Through Coins Denomination
    for coin in coins:
        # Looks for the Minimum 
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Returns True if Change Can be Made, False if Change Cannot be Made
    return dp[amount] != float('inf') and dp[amount] <= limit 


coins = [1, 2, 5, 10]
amount = 3
limit = 2

# Expected: True
print(coinChange(coins, amount))
# Expected: True
print(coinChangeLimit(coins, amount, limit))

coins = [5, 10, 25]
amount = 3
limit = 2

# Expected: False
print(coinChange(coins, amount))
# Expected: False
print(coinChangeLimit(coins, amount, limit))

coins = [5, 10, 25]
amount = 15
limit = 1

# Expected: True
print(coinChange(coins, amount))
# Expected: False
print(coinChangeLimit(coins, amount, limit))
