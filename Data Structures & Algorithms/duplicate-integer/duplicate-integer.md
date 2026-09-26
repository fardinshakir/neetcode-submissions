# 217. Contains Duplicate

**Problem:** Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

```
Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false
```

## Attempt 1

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = {}
        for n in nums:
            if n not in numbers:
                numbers[n] = 1
            else:
                return True

        return False
```

**Approach (my explanation):** Create a hashmap to count occurrences of each number. Iterate through the list — if a number isn't in the map yet, add it with a counter. If it's already there, that means it's a duplicate, so return True. Otherwise return False.

### Q&A

**Q: What's the time and space complexity?**
A: O(n) time and space.

**Q: You're using the hashmap values as counters, but do you ever actually use that count? What does that suggest about the data structure choice?**
A: I don't actually need the stored counter, so it's not necessary — a set would work just as well.

**Q: What does your function return for an empty list, or a list with one element?**
A: It should return `False` for both an empty list and a single-element list.

**Follow-up: Would switching to `len(set(nums)) != len(nums)` be better, worse, or the same, and why?**
A (initial): It would be better, since it's O(1) time and space.
*(Correction: `set(nums)` still has to iterate through all n elements and can store up to n of them — that's O(n) time and O(n) space, same complexity class as the original, not O(1).)*

**Follow-up: Trace through `[1,1,2,3,4,5]` — does either version do less work?**
A (initial): The set version does less work.
*(Clarified through tracing: both versions do the same work per element — check, then add. The actual difference is that the loop version can return `True` the moment it hits a duplicate, while `len(set(nums))` always has to scan the entire array first before it can compare lengths — it has no way to stop early.)*

**Follow-up: So is version A's O(n) smaller than version B's O(n)?**
A (initial): So A's O(n) is less than B's O(n)?
*(Corrected: Big-O is a category describing worst-case growth, not a precise ranking — both are O(n) worst-case. The accurate way to phrase it: "both are O(n) worst-case, but A has better best/average-case performance since it can exit early, while B always does a full pass." I described this using an infinity-comparison analogy, which captures the right intuition but isn't the phrasing to use in an actual interview, since it could sound like a misunderstanding of complexity classes.)*

## Final Solution

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
```

**Complexity:** O(n) time, O(n) space

## Areas for Improvement

- Jumped to "O(1)" for `set(nums)` without tracing through what the constructor actually costs — worth being more careful before naming a complexity class.
- Conflated "shorter/cleverer code" with "better complexity" at first — these are independent, and a one-liner isn't automatically faster.
- Needed a couple of passes to clearly separate "same worst-case complexity class" from "different practical/average-case performance" — useful phrasing to have ready: *"same complexity class, but mine can short-circuit in the average case."*
