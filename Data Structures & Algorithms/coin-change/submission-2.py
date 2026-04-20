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
                if amount - coin in seen.keys():
                    return_value = seen[amount - coin]
                else:
                    return_value = recurse(amount - coin)
                if return_value >= 0:
                    # Store smallest found for amount - current_coin
                    # Check if using this coin has given the least amount of coins
                    smallest = min(smallest, return_value + 1)

            if smallest == math.inf:
                seen[amount] = -1
            else:
                seen[amount] = smallest
            
            return seen[amount]
                
        return recurse(amount)

        # find the largest and continue getting the largest until you get the one
        # Wrong e.g. amount = 18, coins = [1, 10, 9]



        
