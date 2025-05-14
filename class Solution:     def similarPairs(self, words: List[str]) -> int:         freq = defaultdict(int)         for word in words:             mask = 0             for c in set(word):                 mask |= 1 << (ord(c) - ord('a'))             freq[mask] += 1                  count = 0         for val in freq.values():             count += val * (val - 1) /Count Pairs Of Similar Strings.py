class Solution:
    def similarPairs(self, words: List[str]) -> int:
        freq = defaultdict(int)
        for word in words:
            mask = 0
            for c in set(word):
                mask |= 1 << (ord(c) - ord('a'))
            freq[mask] += 1
        
        count = 0
        for val in freq.values():
            count += val * (val - 1) // 2
        return count
