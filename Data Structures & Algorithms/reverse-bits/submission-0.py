class Solution:
    def reverseBits(self, n: int) -> int:
        n_string = f"{n:032b}"
        print(n_string)
        n_string_reversed = n_string[::-1]
        print(n_string_reversed)
        return int(n_string_reversed, 2)