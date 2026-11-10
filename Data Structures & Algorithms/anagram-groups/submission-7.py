class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            l[sortedS].append(s)
        return list(l.values())