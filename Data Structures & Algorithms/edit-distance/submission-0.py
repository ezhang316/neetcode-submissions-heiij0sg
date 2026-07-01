import math
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        memo = {}

        def rec(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i >= len(word1) and j >= len(word2):
                memo[(i, j)] = 0
                return memo[(i, j)]

            if i >= len(word1):
                operations = rec(i, j + 1) + 1
            elif j >= len(word2):
                operations = rec(i + 1, j) + 1
            elif word1[i] == word2[j]:
                operations = rec(i + 1, j + 1)
            else:
                operations1 = rec(i, j + 1) + 1

                operations2 = rec(i + 1, j) + 1

                operations3 = rec(i + 1, j + 1) + 1
                operations = min(operations1, operations2, operations3)

            memo[(i, j)] = operations
            return memo[(i,j)]
        
        return rec(0,0)