class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        card_count = collections.defaultdict(int)

        for card in hand:
            card_count[card] += 1
        
        keys_sorted = sorted(card_count.keys())

        for key in keys_sorted:
            if card_count[key] < 1:
                continue
            
            while card_count[key] > 0:
                for i in range(groupSize):
                    if card_count[key + i] == 0:
                        return False
                    card_count[key + i] -= 1
        
        return True

        

