class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq = {}

        for i in arr:
            freq[i] = freq.get(i, 0) + 1

        a = list(freq.values())
        s = set(freq.values())

        return sum(a) == sum(s)