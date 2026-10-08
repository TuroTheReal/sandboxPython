# Lesson 0: Big-O

Big-O answers ONE question: when the input doubles, how much more time does
my code take? (or how much more memory?)

It's not a stopwatch. It's a growth rate. Ignore constants and small terms,
keep the dominant term:

    3n + 5      -> O(n)
    n² + 100n   -> O(n²)     (for large n, n² crushes 100n)
    2           -> O(1)

## Counting, concretely

1. A loop over n elements                  -> O(n)
2. A loop INSIDE a loop (n x n)            -> O(n²)
3. Two loops one AFTER the other           -> O(n) + O(n) = O(n), NOT O(n²)
4. Halving the problem at each step        -> O(log n)
5. Sorting                                 -> O(n log n)

Classic trap: `y in my_list` isn't free, it's O(n) (Python walks the list).
Put it in a loop and you get a hidden O(n²). The same test on a `set` is O(1).

## The optimization move (your "A to Z optimization")

    # Brute force: for each element, search in the list
    for i in range(n):          # O(n)
        for j in range(n):      # x O(n)
            ...                 # => O(n²)

    # Optimized: a hashmap to remember what we've already seen
    seen = set()                # O(n) memory
    for x in nums:              # O(n)
        if needed in seen: ...  # O(1) lookup
        seen.add(x)             # => O(n) total

We traded memory (the set) for speed. That's the time/space tradeoff, and
it's what interviewers want to hear you explain.

## Your exercise

Open `bigo_exercises.py`. For each function, write as a comment:

- the TIME complexity
- the SPACE complexity (extra memory, excluding the input)
- why, in one line

Don't guess by feel: count the loops, spot the `in list`, the sorts.
When you've done all 7, tell me and we'll correct them together.
