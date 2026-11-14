class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        result = ""
        for s in strs:
            result = result + s + "#"
        return result

    def decode(self, s: str) -> List[str]:
        if len(s) == 1:
            return [s]
        return s[:len(s)-1].split("#")