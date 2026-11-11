class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        res = [0] * (len(num1) + len(num2))

        num1, num2 = num1[::-1], num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                prod = int(num1[i]) * int(num2[j])
                res[i + j] += prod
                res[i + j + 1] += res[i + j] // 10
                res[i + j] = res[i + j] % 10
        
        res = res[::-1]
        i = 0
        while res[i] == 0:
            i += 1
        
        res = res[i:]

        res = list(map(str, res))
        
        return "".join(res)