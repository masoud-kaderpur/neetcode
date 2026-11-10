class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # 1,1,2,2,2,3
        # 1: 2
        # 2: 3
        # 3: 1
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        arr = {}
        # 2: 1
        # 3: 2
        # 1: 3
        for n, c in count.items():
            arr[c] = n

        l = []
        for k in sorted(arr.keys(), reverse=True):
            l.append(arr[k])
            if(len(l) == k):
                return l

        return l