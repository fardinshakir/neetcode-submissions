# 1. Two Sum

**Problem:** Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to `target`. You may assume each input has exactly one solution, and you may not use the same element twice.

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]   // because nums[0] + nums[1] == 9
```

## Attempt 1 (final)

```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, n in enumerate(nums):
        desired = target - n
        if desired in seen:
            return [seen[desired], i]
        seen[n] = i
```

### Q&A

**Q: What's the time and space complexity?**
A (initial): O(n) time — since we have to iterate through the array once.
*(Space initially answered as O(1): "O(1) complexity." Corrected after prompting: the `seen` dictionary can grow to hold up to n entries in the worst case, so space is actually O(n), not O(1).)*

**Q: Why do you check `if desired in seen` before adding `seen[n] = i`, rather than after? What could go wrong if the order were flipped?**
A: If `desired` is already in `seen`, we can return early without needing to continue. If we added `n` to `seen` first, and the desired value happened to equal the current number, it would end up matching the number against itself — reusing the same index.

**Q: Trace `nums = [3, 3]`, `target = 6` as if the order were flipped (add to `seen` first, then check) — what would happen?**
A: On the first iteration, it would add `3` to `seen` at index 0, then immediately check if `desired` (3) is already in `seen` — and it would be, since it was just added. That would incorrectly return `[0, 0]`, reusing the same index twice.

**Q: Now trace the actual code (check-then-add order) on the same input — what's the real output?**
A: For the first `3`, it hasn't been seen before, so it gets added as `{3: 0}`. For the second `3`, `desired` (3) is already in `seen`, so it returns `[0, 1]` — using the previously stored index and the current index. Correct.

**Q: What does your function return if no valid pair exists? Is that a problem given the problem's constraints?**
A: I'd return `[]` in that case, though it's not really a concern since the problem guarantees exactly one solution always exists.

## Final Solution

```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, n in enumerate(nums):
        desired = target - n
        if desired in seen:
            return [seen[desired], i]
        seen[n] = i
```

**Complexity:** O(n) time, O(n) space

## Areas for Improvement

- Correct, optimal one-pass hashmap solution on the first attempt — no bugs, no false starts.
- Initially misjudged space complexity as O(1), overlooking that the `seen` dictionary is itself an O(n) auxiliary structure. Worth double-checking any data structure being built alongside the input, not just the input itself, when asked for space complexity.
- Solid reasoning on check-before-insert ordering and return-type consistency (`[]` over `False`) without needing much prompting.
