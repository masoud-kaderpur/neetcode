class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # 3,0,1,0
        # 3: 1
        # 0: 2
        # 1: 1
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        arr = {}
        # 1: 3
        # 2: 0
        # 1: 1
        for n, c in count.items():
            if c not in arr:
                arr[c] = []
            arr[c].append(n)

        l = []
        for k in sorted(arr.keys(), reverse=True):
            for i in arr[k]:
                l.append(i)
                if(len(l) == k):
                    return l

        return l