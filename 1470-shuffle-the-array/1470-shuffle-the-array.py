class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        a = nums[:n]
        b = nums[n:]

        for i in range(n):
            res.append(a[i])
            res.append(b[i])

        return res