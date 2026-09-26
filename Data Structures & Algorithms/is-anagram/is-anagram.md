# 242. Valid Anagram

**Problem:** Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

```
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
```

## Attempt 1 (broken)

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = s.split()
        t = t.split()

        if s.sort() == t.sort():
            return True
        return False
```

**Issue:** `.split()` on a string with no delimiter returns a single-element list (the whole word), not individual characters. `.sort()` sorts a list in place and returns `None`, so `s.sort() == t.sort()` is really comparing `None == None`, which is always `True` regardless of input. Solution abandoned.

## Attempt 2

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return false  # bug: should be False
        anagram = []
        for i, letter in enumerate(s):
            if letter in t and s.count(letter) == t.count(letter):
                anagram.append(True)
        if len(anagram) != len(s):
            return False
        return True
```

### Q&A

**Q: Line 4 has `return false` — what happens when Python hits that line?**
A: It returns `False`.
*(Note: this was actually a bug — lowercase `false` isn't defined in Python and would raise a `NameError`. Fixed to `False`.)*

**Q: What's the time complexity, given `.count()` is called inside a loop that iterates over the string?**
A: O(n²) — since `.count()` itself is O(n), and it's called inside a loop that also runs n times.

**Q: Trace `s = "aa"`, `t = "aa"` — what does `anagram` end up containing?**
A (initial): It would return `True`, and `anagram` would be `[True]`.
*(Corrected after tracing: the loop runs once per character in `s`, not once per unique letter. Since `s` has two `'a'`s, the loop runs twice, and `anagram` ends up as `[True, True]` — length 2, matching `len(s)`. The final answer is still correct, but the earlier reasoning about the loop only running once was wrong.)*

**Q: Trace `s = "ab"`, `t = "aa"` — does the function correctly return False?**
A: Yes — for the letter `'a'`, `s.count('a')` is 1 and `t.count('a')` is 2, so nothing gets appended for `'a'`. Since `anagram` ends up shorter than `s`, the length check catches the mismatch and returns `False`.

## Attempt 3

```python
if sorted(s) == sorted(t):
    return True
return False
```

### Q&A

**Q: What's the time complexity of `sorted(s)`?**
A (initial): O(n).
*(Corrected: `sorted()` is a comparison-based sort — Python uses Timsort — which runs in O(n log n), not O(n). No comparison-based sort can beat O(n log n) in the general case.)*

**Q: Given that, what's the overall complexity of this solution — better, worse, or the same as the `.count()` version?**
A: O(n log n) — better than the earlier O(n²) approach, since it avoids the nested counting, but not yet O(n).

## Attempt 4 (final)

```python
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = {}

    for letter in s:
        count[letter] = count.get(letter, 0) + 1

    for letter in t:
        if letter not in count:
            return False
        count[letter] -= 1

    return not any(count.values())
```

**Approach (my explanation):** Build a shared counter — add to it for every letter in `s`, then subtract for every letter in `t`. If everything nets out to 0, the strings are anagrams.

### Q&A

**Q: How does `not any(count.values())` work — what counts as truthy for an integer?**
A: Any nonzero integer is truthy — positive or negative.

**Q: Trace `s = "aa"`, `t = "ab"` — does this correctly return False?**
A: After processing `s`, the counter is `{'a': 2}`. After processing `t`, it becomes `{'a': 1, 'b': -1}`. Since both values are nonzero, `any()` returns `True`, and `not any(...)` returns `False` — correctly identifying these as not anagrams.

**Q: Is the length check at the top still necessary, given the `if letter not in count: return False` check in the second loop?**
A: Not strictly necessary for correctness, but I'd keep it as an early check.
*(Elaboration: it's a redundant-but-useful O(1) short-circuit — it avoids doing a full O(n) pass on two strings that obviously can't match, since a mismatched-length counter would still get caught by `any()` at the end anyway, just after more unnecessary work.)*

**Q: Final time/space complexity?**
A: O(n) time, O(n) space — for the counter dictionary.

## Areas for Improvement

- Capitalization bug (`false` vs `False`) — a small but real Python gotcha that would cause a crash, not just a wrong answer.
- Misjudged `.count()` inside a loop as linear instead of recognizing the nested-loop cost (O(n²)).
- Initially misjudged `sorted()` as O(n) instead of O(n log n) — worth remembering comparison-based sorts have a hard floor of O(n log n).
- Needed to trace through loop iterations carefully more than once — good habit to slow down and verify assumptions about how many times a loop runs, especially with repeated characters.
- Good final instinct to move from sorting to a frequency-counter approach without much prompting, landing on the optimal O(n) solution.
