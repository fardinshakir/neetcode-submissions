# 49. Group Anagrams

**Problem:** Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["eat","tea","ate"]]
```

## Attempt 1 (final)

```python
anagrams = defaultdict(list)
for word in strs:
    sorted_word = ''.join(sorted(word))
    anagrams[sorted_word].append(word)

return list(anagrams.values())
```

### Q&A

**Q: State time and space complexity precisely — there's an outer loop over `strs` (length n) and an inner sort of each word (max length k). How do those combine?**
A (initial): O(n log n) time, O(n) space — iterating is n, and the sort is log n.
*(Corrected after prompting: sorting a single word of length k costs O(k log k), and this happens once per word across n words, so the total time is O(n · k log k), not O(n log n). Space was also refined from O(n) to O(nk), since both the original words and their sorted-string keys are stored, and each can be up to length k.)*

**Q: Why does sorting the word work as a grouping key? What property of anagrams makes this valid?**
A: All anagrams produce the same sorted result, since they contain the same letters in the same quantities — just rearranged. That makes the sorted form a valid shared key for grouping them.

**Q: Why use `defaultdict(list)` instead of a plain `dict`?**
A: With a plain dict, I'd have to check whether the sorted-word key already exists before appending to it. `defaultdict(list)` automatically initializes a new empty list for any key I haven't seen yet, so I can just append directly without that check.

**Q: Can you think of a way to build the grouping key without sorting — something that gets you from O(k log k) per word down to O(k)?**
A: I'd create a fixed-size array of 26 zeros (one slot per letter a–z), loop through each word once, and increment `counter[ord(char) - ord('a')]` for each character — `ord(char) - ord('a')` maps a letter to an index 0–25. Then convert the counter array to a tuple so it can be used as a dictionary key, and use that tuple as the key in the same `defaultdict(list)` structure.

**Q: What complexity would that counting approach get you?**
A (initial): O(n log k) time, O(nk) space.
*(Corrected: building a 26-length counter for one word costs O(k), not O(k log k) — there's no sorting involved. Doing that for n words gives a total time of O(n · k), which is strictly better than the sorting approach. Space remains O(nk), same as before.)*

## Final Solution

```python
anagrams = defaultdict(list)
for word in strs:
    sorted_word = ''.join(sorted(word))
    anagrams[sorted_word].append(word)

return list(anagrams.values())
```

**Complexity:** O(n · k log k) time, O(nk) space (n = number of words, k = max word length)

**Optimal alternative (discussed, not implemented):** 26-length frequency-count array per word as the key, instead of sorting — reduces time to O(n · k), same O(nk) space.

## Areas for Improvement

- Correct, clean solution on the first attempt, with good reasoning for choosing `defaultdict` over a plain dict.
- Needed a couple of passes to state multi-variable complexity correctly — initially defaulted to single-variable notation (e.g., "O(n log n)") instead of accounting for both the number of words (n) and word length (k) separately. Worth practicing stating complexities like "O(n · k log k)" directly, rather than starting with a simpler-but-wrong version.
- Strong pattern recognition — connected this problem back to the letter-frequency-counter idea from Valid Anagram without much prompting, and correctly derived the more optimal O(nk) alternative.
