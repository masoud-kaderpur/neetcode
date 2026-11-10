class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        arr = {}
        for n, c in count.items():
            if c not in arr:
                arr[c] = []
            arr[c].append(n)

        l = []
        for c in sorted(arr.keys(), reverse=True):
            for n in arr[c]:
                l.append(n)
                if(len(l) == k):
                    return l

        return l