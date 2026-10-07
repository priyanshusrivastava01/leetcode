class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = []
        a = []

        for i in range(len(nums)):
            ans.append(nums[i])

        for i in range(len(nums)):
            a.append(nums[i])

        ans.extend(a)
        return ans