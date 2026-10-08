# CHEATSHEET

Your quick reference. Reopen it during every problem.

## Big-O: how it grows when the input grows

Ignore constants, keep the dominant term. `3n + 5` becomes `O(n)`.

| Class       | Name           | Typical example                        | n=1000 -> ops |
|-------------|----------------|----------------------------------------|---------------|
| O(1)        | constant       | dict/set access, `list[i]`, arithmetic | 1             |
| O(log n)    | logarithmic    | binary search (halving)                | ~10           |
| O(n)        | linear         | one pass                               | 1 000         |
| O(n log n)  | linearithmic   | `sorted()`, divide and conquer         | ~10 000       |
| O(n²)       | quadratic      | nested double loop                     | 1 000 000     |
| O(2^n)      | exponential    | recursion that explores everything     | astronomical  |

From best (top) to worst (bottom). In interviews, you often start from an
O(n²) and bring it down to O(n) with a hashmap. That's THE move.

## Python toolkit: structures and complexities

| Operation                       | list         | dict / set    | deque          |
|---------------------------------|--------------|---------------|----------------|
| index access `x[i]`             | O(1)         | -             | O(1) at ends   |
| lookup `y in x`                 | O(n)  TRAP   | O(1) average  | O(n)           |
| append at end `.append()`       | O(1) amort.  | O(1) (`add`)  | O(1)           |
| insert/remove at head           | O(n)         | -             | O(1)           |
| remove `.pop()`                 | O(1) at end  | O(1)          | O(1) at ends   |

`y in a_list` is O(n): that's trap #1. If you test membership in a loop,
convert to a `set` first -> O(1).

## Reflexes that turn an O(n²) into an O(n)

- "Have I already seen X?"               -> `set` (O(1) lookup)
- "How many times does X appear?"        -> `collections.Counter`
- "A counter per key without KeyError"   -> `collections.defaultdict(int)`
- "Queue with both ends"                 -> `collections.deque`
- Sorting: `sorted(x)` is O(n log n), never O(n). There's no free sort.

## Time vs Space

A hashmap costs O(n) memory to save time. That's the classic tradeoff:
you trade space for speed. In interviews, ALWAYS state both:
`# Time: O(n)  Space: O(n)`.
