class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        for i in range(32):
            aBit = (a >> i) & 1
            bBit = (b >> i) & 1
            
            sum_bit = aBit ^ bBit ^ carry
            carry = (aBit + bBit + carry) >= 2

            if sum_bit:
                res |= sum_bit << i

        mask = 0xFFFFFFFF

        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)
        
        return res