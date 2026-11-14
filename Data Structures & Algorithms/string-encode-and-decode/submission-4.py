class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result = result + s + "#"
        return result

    def decode(self, s: str) -> List[str]:
        return s[:len(s)-1].split("#")