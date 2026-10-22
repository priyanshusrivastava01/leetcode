# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums)
#         total = (n*(n+1)) //2
#         summ = 0
#         for i in range(n):
#             summ += nums[i]

#         return total - summ
        

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n*(n+1)) //2
        return total - sum(nums)