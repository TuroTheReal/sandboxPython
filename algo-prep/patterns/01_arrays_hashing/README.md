# Pattern 1: Arrays & Hashing

## The idea in one sentence

When you're tempted to traverse the list AGAIN inside a loop (so O(n²)),
replace that search with a hashmap (`dict` / `set`): O(1) lookup, and the
whole thing drops to O(n). It's the reflex from #6 of the Big-O exercise.

## The signals that say "it's this pattern"

- "is there a duplicate?"
- "count the occurrences of..."
- "have I already seen X?"
- "two elements whose sum is K"
- "group anagrams / identical elements"

As soon as you think "I'd need to find something seen earlier", hashmap.

## Your tools

| Need                               | Tool                        | Lookup |
|------------------------------------|-----------------------------|--------|
| "have I already seen X?"           | `set`                       | O(1)   |
| "how many times X?"                | `collections.Counter`       | O(1)   |
| "accumulate per key, no KeyError"  | `collections.defaultdict`   | O(1)   |
| "map a value to a key"             | `dict`                      | O(1)   |

## Demo (throwaway example, not an exercise)

Count each character of a string.

    # BRUTE FORCE: for each letter, recount the whole string
    #   s.count(c) is O(n), inside a loop => O(n²)
    #
    # OPTIMIZED: a single pass, increment a counter on the fly

    def count_letters(s: str) -> dict[str, int]:
        counter: dict[str, int] = {}
        for c in s:                             # O(n)
            counter[c] = counter.get(c, 0) + 1  # dict get + set = O(1)
        return counter
    # Time: O(n)   Space: O(k), k = number of distinct characters

The skeleton is always the same: **a single pass + a dict/set to remember
on the fly**. You'll redo it several times.

(`collections.Counter(s)` does it in one line. But understand the manual
version first: it's the one you'll be asked to write on the whiteboard.)

## LeetCode problems

The full easy/medium/hard list for this pattern is in `../../PROBLEMS.md`
(section "1. Arrays & Hashing"). Start with the 3 easy ones (#217, #242, #1),
move on to the medium ones when the reflex is there.

On leetcode.com, without looking at the solution. Paste me your code + its
complexity (Time + Space) after each one, I review. Goal: aim for O(n).
