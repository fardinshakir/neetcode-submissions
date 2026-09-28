# 347. Top K Frequent Elements

**Problem:** Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

## Attempt 1 (final)

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        container = {}
        for n in nums:
            if n not in container:
                container[n] = 1
            container[n] += 1
        container = list(container.items())
        container.sort(key=lambda x: x[1], reverse=True)
        freq = []
        for n in container:
            freq.append(n[0])
        return freq[:k]
```

### Q&A

**Q: Trace the counting loop on `nums = [1,1,1,2,2,3]` — what does `container` look like after it, and does each count match how many times that number actually appears?**
A (initial): `container` would be `{1: 3, 2: 2, 3: 1}`.
*(Corrected after tracing: the `+= 1` line sits outside the `if`, so it runs on every element, including the first time a number is seen. The actual result is `{1: 4, 2: 3, 3: 2}` — every count is one higher than the true frequency. The bug didn't affect the final answer because every count is inflated by the same amount, so the relative ranking is unchanged — but it's a real bug, not a correct-by-design behavior.)*

**Q: Does the final answer still come out right despite this?**
A: Yes — after converting to a list of tuples and sorting by count (descending), the top-k order is unaffected by the uniform +1 offset.

**Q: State time and space complexity.**
A (initial): O(n log n) time, dominated by `container.sort()`. O(n) space, "because we only work with 1D arrays."
*(Space reasoning corrected: the justification isn't "1D arrays" — it's that the dict can hold up to n distinct keys, and the resulting list of tuples can also hold up to n entries.)*

**Q: The problem's follow-up asks for better than O(n log n) — any ideas?**
A: Not sure — I know a heap arranges elements based on how it maps the data, but that's about as far as I could get.
*(Not implemented. Discussed but left as a follow-up: bucket sort using frequency as the bucket index for O(n), or a min-heap of size k for O(n log k). Heap detail clarified: a heap doesn't keep everything fully sorted — a min-heap only guarantees the smallest element is on top, which is exactly what's needed to efficiently evict the smallest when the heap exceeds size k.)*

**Q: Tidier way to build the final list before slicing `[:k]`?**
A: Not sure.
*(Suggested: `[n for n, _ in container[:k]]`, or `Counter(nums).most_common(k)` as a built-in, with the caveat that an interviewer may ask for it without library shortcuts.)*

## Final Solution (as submitted, with known bug)

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        container = {}
        for n in nums:
            if n not in container:
                container[n] = 1
            container[n] += 1
        container = list(container.items())
        container.sort(key=lambda x: x[1], reverse=True)
        freq = []
        for n in container:
            freq.append(n[0])
        return freq[:k]
```

**Complexity:** O(n log n) time (sort-dominated), O(n) space

**Known bug:** counting loop inflates every count by 1 (`container[n] += 1` runs unconditionally, not just in the `else` branch). Doesn't affect output correctness here, but should be fixed with `container[n] = container.get(n, 0) + 1` or a proper `if/else`.

**Optimal alternative (not implemented):** bucket sort by frequency for O(n) time, or a size-k min-heap for O(n log k) time.

## Areas for Improvement

- Off-by-one-style counting bug (`+=` outside the conditional) — masked by the fact that a uniform offset doesn't change relative ranking, but worth catching in review since it wouldn't survive a task that used the raw counts for anything else.
- Space complexity justification needs work — name the actual data structure that scales with input (dict/list), not an unrelated property like dimensionality.
- Didn't push through to the optimal O(n) bucket-sort solution in-session — flagged to revisit independently, since "can you beat O(n log n)" is the standard, expected follow-up on this exact problem.
