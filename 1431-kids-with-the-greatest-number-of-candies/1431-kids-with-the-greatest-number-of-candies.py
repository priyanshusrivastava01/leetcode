class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxi = max(candies)

        for i in range(len(candies)):

            if candies[i]+extraCandies >= maxi:
                candies[i] = True
            else:
                candies[i] = False

        return candies