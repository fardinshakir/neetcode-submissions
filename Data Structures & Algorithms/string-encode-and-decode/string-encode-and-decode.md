# 271. Encode and Decode Strings

**Problem:** Design an algorithm to encode a list of strings to a single string, and decode that string back to the original list of strings. Strings may contain arbitrary characters, including whatever delimiter is chosen.

```
Input: ["neet","code","love","you"]
Output after encode: some single string
Output after decode: ["neet","code","love","you"]
```

## Attempt 1 (final)

```python
class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + '#' + word
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            i = j + 1
            result.append(s[i:i + length])
            i += length
        return result
```

**Approach (my explanation):** Use length-prefixing instead of a plain delimiter, so a character like `#` appearing inside a word doesn't break the parsing. Encode each word as `{length}#{word}`. To decode, walk through the string: find the next `#` starting from the current position, read everything before it as the length, then read exactly that many characters after the `#` as the next word, and advance the pointer accordingly.

### Q&A

**Q: Trace `strs = ["a#b", "c"]` through both `encode` and `decode` — does it handle the `#` inside a word correctly?**
A: Encoding gives `'3#a#b1#c'`. Decoding: starting at index 0, look for the next `#` — found right after the digit `3`, so the length is `3`. Move the pointer to just after that `#`, then read exactly 3 characters (`a#b`) as the word, regardless of the `#` inside it. Advance the pointer past those 3 characters, and repeat for the next word (`c`, length 1). Correct.

**Q: Why is `s.find('#', i)` guaranteed to find the *length delimiter* and never a `#` inside a word's content?**
A: Because the encoding explicitly places the first `#` immediately after the length digits, and the search always starts at `i`, which is set to exactly where a new length prefix begins. Since the pointer only ever stops at word boundaries, the `#` it finds is always the one that was placed as a delimiter, not one embedded in a word.

**Q: State time and space complexity for both functions — is there anything about repeated string concatenation in Python worth flagging?**
A (initial): O(n) time and space for both `encode` and `decode`.
*(Corrected for `encode`: `result += ...` inside a loop is a real Python gotcha. Strings are immutable, so each `+=` call copies the entire existing string plus the new piece into a brand-new string object — it does not modify `result` in place. Summed across the whole loop, this makes `encode` O(L²) in the total character count, not O(L) — and this isn't a rare worst-case input, it's the actual cost on every input due to how string immutability works. Initially misjudged as "worst case, but safe to call O(n)" — corrected to recognize this is the guaranteed behavior, not an edge case. `decode`'s O(n) time/space was correctly reasoned — list appends are amortized O(1), and the result list can hold up to n entries.)*

**Q: What's the standard fix for this pattern?**
A: Build a list of pieces — e.g., `f"{len(word)}#{word}"` per word — and use `''.join(...)` at the end instead of repeated `+=`.

**Q: Trace `strs = []` and `strs = [""]` through the actual code.**
A: For `[]`, the loop never runs, so `encode` returns `""`. Decoding `""`: the while loop condition (`i < len(s)`) is false immediately, so it returns `[]` — round-trips correctly. For `[""]`, `encode` returns `"0#"`. Decoding: `find('#', 0)` locates it at index 1, `length = int(s[0:1]) = 0`, pointer moves to index 2, `s[2:2]` appends `""` to the result, pointer advances by 0. Loop ends, returns `[""]` — round-trips correctly.

## Final Solution

```python
class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + '#' + word
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            i = j + 1
            result.append(s[i:i + length])
            i += length
        return result
```

**Complexity:** `encode` — O(L²) time as written (due to repeated `+=`), fixable to O(L) with list + `.join()`; O(L) space. `decode` — O(L) time and space, where L is the total character count across all strings.

## Areas for Improvement

- Core algorithmic idea (length-prefixing to survive arbitrary characters, including the delimiter itself) was correct and well-explained on the first attempt — this is the key insight the problem is testing, and no prompting was needed to arrive at it.
- Real complexity bug in `encode`: repeated string concatenation in a loop is O(n²)/O(L²), not O(n) — a classic, frequently-tested Python-specific gotcha. Worth internalizing that this is a guaranteed cost of the pattern itself, not something that only shows up on adversarial inputs — "worst case" language should be reserved for input-dependent behavior, not for a cost that's baked into every run.
- Correctly named the standard fix (list + `.join()`) and correctly traced both edge cases once asked directly, with no errors.
