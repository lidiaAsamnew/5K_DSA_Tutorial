class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs: 
            count = {}
            for char in s:
                count[char] = count.get(char, 0) + 1

            tup = tuple(sorted(count.items()))

            if tup in groups:
                groups[tup].append(s)
            else:
                groups[tup] = [s] 
            
        return list(groups.values())
