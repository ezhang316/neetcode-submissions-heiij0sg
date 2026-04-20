class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # starting with any coin
        # add 1 to coin count
        # and repeat function call with amount - coin
        # for any amount, store the smallest amount in seen


        seen = {}
        
        def recurse(amount):
            if amount < 0:
                return -1
            if amount == 0:
                return 0
            
            nonlocal seen
            print(seen)
            if amount in seen.keys():
                return seen[amount]
            
            # Calculate smallest for given amount
            smallest = math.inf
            nonlocal coins
            for coin in coins:
                return_value = recurse(amount - coin)
                if return_value >= 0:
                    # Store smallest found for amount - current_coin
                    # Check if using this coin has given the least amount of coins
                    smallest = min(smallest, return_value + 1)

            if smallest == math.inf:
                return -1

            seen[amount] = smallest
            return smallest
                
        return recurse(amount)


        
