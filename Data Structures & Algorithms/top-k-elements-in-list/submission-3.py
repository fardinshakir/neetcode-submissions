class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        container = {}
        for n in nums:
            if n not in container:
                container[n] = 1
            else:
                container[n] += 1
        container = list(container.items())
        container.sort(key=lambda x: x[1], reverse=True)
        freq = []
        for n in container:
            freq.append(n[0])
        return freq[:k]

        