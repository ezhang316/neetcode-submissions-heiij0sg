class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        
        count = dict(Counter(s))
        res = []
        length = 0
        seen = set()
        for c in s:
            
            length += 1
            count[c] -= 1
            seen.add(c)

            if count[c] == 0:
                seen.remove(c)
            if not seen:
                res.append(length)
                length = 0
        
        return res