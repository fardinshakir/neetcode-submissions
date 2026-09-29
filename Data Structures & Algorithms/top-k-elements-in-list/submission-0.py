class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        q = sorted(count.items(), key = lambda item: item[1], reverse=True)
        answers = []
        for numbers in q:
            answers.append(numbers[0])
        return answers[:k]