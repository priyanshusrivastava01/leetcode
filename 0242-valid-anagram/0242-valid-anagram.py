# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         a = sorted(s)
#         b = sorted(t)
#         count = 0
#         for i in range(len(s)):
#             if a[i] == b[i]:
#                 count += 1
#         return count == len(s)
        

class Solution:
    def isAnagram(self, s: str, t: str):
        freq1 = {}
        freq2 = {}

        for i in s:
            freq1[i] = freq1.get(i, 0) + 1
        
        for j in t:
            freq2[j] = freq2.get(j, 0) + 1

        return freq1 == freq2