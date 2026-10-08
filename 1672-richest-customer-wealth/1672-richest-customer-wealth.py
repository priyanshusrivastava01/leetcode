class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        maxi = 0

        for i in range(len(accounts)):
            total = 0

            for j in range(len(accounts[0])):
                total += accounts[i][j]
            maxi = max(maxi, total)

        return maxi